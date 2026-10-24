
# # =====================================================================
# # Lab11 - PyTorch Basics
# # =====================================================================
# # Setup:  pip install torch numpy
# # Run:    python Lab11_PyTorch.py
# #
# # What we cover:
# #   1. Tensor        -> PyTorch's array-like data structure
# #   2. Autograd      -> PyTorch calculates gradients automatically
# #   3. Training loop -> Forward pass, loss, gradient, and weight update
# #
# # =====================================================================

import numpy as np
import torch


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# # ---------------------------------------------------------------------
# section("1. Tensors - PyTorch's array-like data structure")
# ---------------------------------------------------------------------
# A tensor is a multidimensional array of numbers.
#   0-D tensor = single number
#   1-D tensor = list of numbers
#   2-D tensor = table of rows and columns
#   3-D/4-D    = can represent images and batches of images

# These are examples of how tensors can represent data.
# The number of dimensions is called the tensor's rank.

# torch_prices = torch.tensor([50.0,67.0,89.9])
# result = torch_prices - 3

# print(result)

# price = torch.tensor(50.0)          # 0-D
# house = torch.tensor([1200.0, 3.0]) # 1-D
# houses = torch.tensor([
#     [1200.0, 3.0],
#     [1500.0, 3.0],
#     [800.0, 2.0]
# ])                                  # 2-D

# print("single number:", price, "| shape:", price.shape)
# print("one house    :", house, "| shape:", house.shape)
# print("many houses  :\n", houses, "\nshape:", houses.shape)

# # Ready-made tensors
# print("zeros:", torch.zeros(3))
# print("ones :", torch.ones(2, 2))
# print("random 0-1:", torch.rand(3))  # Often used to initialise weights

# # Basic tensor math
# a = torch.tensor([1.0, 2.0, 3.0])
# b = torch.tensor([10.0, 20.0, 30.0])

# print("a + b :", a + b)  # Element-wise addition
# print("a * b :", a * b)  # Element-wise multiplication
# print("a @ b :", a @ b)  # Dot product = 10 + 40 + 90
# print("mean  :", b.mean(), "| max:", b.max())

# # Indexing and reshape
# print("first column (sqft):", houses[:, 0])
# print("reshape to column  :", a.reshape(-1, 1).shape)  # (3, 1)

# # Data types matter. Many model parameters use float32.
# # Integer tensors are commonly used for class labels and indexes.
# print("dtype:", houses.dtype)  # torch.float32

# # NumPy <-> PyTorch
# # Data often starts in NumPy or Pandas.
# np_data = np.array([1.0, 2.0, 3.0])
# t = torch.from_numpy(np_data).float()

# print("from numpy:", t)
# print("back to numpy:", t.numpy())
# print(".item() gives a Python number:", t.sum().item())

# CPU or GPU
# PyTorch supports CPU and, when available, GPU computation.
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print("running on:", device)

# t = t.to(device)
# print("tensor device:", t.device)

# # NumPy conversion requires a CPU tensor.
# # This works whether the tensor is already on the CPU or on a GPU.
# print("back to numpy after device transfer:", t.cpu().numpy())


# # ---------------------------------------------------------------------
# section("2. Autograd - PyTorch calculates gradients automatically")
# # ---------------------------------------------------------------------

# section("2.1. Pure Python - Manual Gradient Descent")

# Initial setup
# w = 0.0
# x = 1.0
# target = 2.0 # output
# lr = 0.01

# for step in range(2000):
#     # 1. Forward pass: calculate prediction
#     pred = w * x

#     # 2. Compute loss: squared difference from the target
#     loss = (pred - target) ** 2

#     # 3. Calculate the derivative manually
#     grad = 2 * (pred - target) * x   

#     # 4. Update the weight using gradient descent
#     w -= lr * grad 

# print(f"Learned w: {w:.2f}")  # Output: 1.98


# section("2.2. PyTorch - Automatic Gradient Calculation")
# Initial setup
w = torch.tensor(0.0, requires_grad=True)
x = torch.tensor(1.0)
target = torch.tensor(2.0)
lr = 0.01

for step in range(500):
    # 1. Forward pass: calculate prediction
    pred = w * x

    # 2. Compute loss
    loss = (pred - target) ** 2

    # 3. Automatically calculate the gradient
    loss.backward()

    # 4. Update the weight without tracking this update in Autograd
    with torch.no_grad():
        w -= lr * w.grad

    # Gradients accumulate by default, so clear the gradient
    # before the next backward pass.
    w.grad.zero_()

print(f"Learned w: {w.item():.2f}")  # Output: 1.98

