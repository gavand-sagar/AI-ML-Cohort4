# =====================================================================
# Lab12 - Linear Regression in PyTorch: Model, Loss, Optimizer
# =====================================================================
# Every demo below is independent.
# Keep the imports, then comment / uncomment one demo at a time.
#
# Main example: predict exam marks from hours studied
#   hours : 1   2   3   4   5
#   marks : 30  40  50  60  70      -> marks = 10 * hours + 20
# =====================================================================

import torch
import torch.nn as nn


# =====================================================================
# DEMO 1 - Data as tensors
# =====================================================================
# print("\n========== DEMO 1: Data as tensors ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# print("hours:\n", hours)
# print("hours shape:", hours.shape)
# print("marks shape:", marks.shape)

# wrong = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
# print(wrong)

# print(wrong.reshape(-1, 1))
# print("\nwithout inner brackets shape:", wrong.shape)
# print("fixed with reshape(-1, 1)   :", wrong.reshape(-1, 1).shape)

# print("\nTakeaway:")
# print("  - Data must be float tensors.")
# print("  - Shape is (rows, columns) = (samples, features) -> (5, 1).")
# print("  - A flat list (5,) must be reshaped to (5, 1).")


# # =====================================================================
# # DEMO 2 - The model: nn.Linear
# # =====================================================================
# print("\n========== DEMO 2: The model nn.Linear ==========")

# torch.manual_seed(0) # fixes the random numbers
# model = nn.Linear(in_features=1, out_features=1)

# print("intial weight w (without any training):", round(model.weight.item(), 4))
# print("intial bias   b (without any training):", round(model.bias.item(), 4))

# #input
# x = torch.tensor([[3.0]])

# with torch.no_grad():
#     output = model(x).item()

# print("model(3)  :", round(output, 4))

# print("\nTakeaway:")
# print("  - nn.Linear(1, 1) is just: prediction = w * x + b")
# print("  - w and b start random, so first predictions are wrong.")
# print("  - Training = finding good values of w and b.")


# # =====================================================================
# # DEMO 3 - Loss: how wrong is the model?
# # =====================================================================
# print("\n========== DEMO 3: Loss (MSE) ==========")

# y = wx + b
# input x = 3  | real_y = 50??? expectation
# w = 3 assumption
# b = 1 asumption
# pred_y = w x + b = 3 * 3 + 1 = 10
# if (real_y != pred_y )
#  change w???? 30 - 10 = 20
#  w = 4, b = 2
# pred_y = wx + b = 4 *3 + 2 = 14
# if (real_y != pred_y )

# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])
# guess_bad = torch.tensor([[10.0], [10.0], [10.0], [10.0], [10.0]])
# guess_ok = torch.tensor([[28.0], [41.0], [52.0], [59.0], [71.0]])
# guess_perfect = marks.clone()

# loss_fn = nn.MSELoss() # we use this in our pytorch code.

# errors = guess_ok - marks
# print("errors for ok guess:", errors.squeeze().tolist())
# print("squared            :", (errors ** 2).squeeze().tolist())
# print("mean of squared    :", round((errors ** 2).mean().item(), 2))
# print("nn.MSELoss         :", round(loss_fn(guess_ok, marks).item(), 2))

# print("\nloss for bad guess    :", loss_fn(guess_bad, marks).item())
# print("loss for ok guess     :", round(loss_fn(guess_ok, marks).item(), 2))
# print("loss for perfect guess:", loss_fn(guess_perfect, marks).item())

# print("\nTakeaway:")
# print("  - Loss = one number that says how wrong predictions are.")
# print("  - MSE = average of (prediction - actual)^2")
# print("  - Lower is better. 0 means perfect.")
# print("  - Order matters: loss_fn(prediction, actual)")


# # =====================================================================
# # DEMO 4 - Gradient: which direction to move w and b
# # =====================================================================
# print("\n========== DEMO 4: Gradient with loss.backward() ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# model = nn.Linear(1, 1)
# with torch.no_grad():
#     model.weight.fill_(1.0)
#     model.bias.fill_(0.0)

# loss_fn = nn.MSELoss()
# loss = loss_fn(model(hours), marks)

# print("w = 1, b = 0  (too small, correct is w = 10, b = 20)")
# print("loss:", loss.item())
# print("gradient before backward:", model.weight.grad)

# loss.backward()

# print("gradient of w:", model.weight.grad.item())
# print("gradient of b:", model.bias.grad.item())

# print("\nTakeaway:")
# print("  - loss.backward() calculates the gradient for every weight.")
# print("  - Gradient negative -> increase the weight to reduce loss.")
# print("  - Gradient positive -> decrease the weight to reduce loss.")
# print("  - Bigger gradient = loss is more sensitive to that weight.")


# # =====================================================================
# # DEMO 5 - Optimizer: actually change w and b
# # =====================================================================
# print("\n========== DEMO 5: optimizer.step() ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# model = nn.Linear(1, 1)
# with torch.no_grad():
#     model.weight.fill_(1.0)
#     model.bias.fill_(0.0)

# loss_fn = nn.MSELoss()
# lr = 0.01  # control the speed of learing
# optimizer = torch.optim.SGD(model.parameters(), lr=lr)

# loss_before = loss_fn(model(hours), marks)
# loss_before.backward()

# w_old = model.weight.item()
# grad_w = model.weight.grad.item()

# optimizer.step()

# w_new = model.weight.item()
# loss_after = loss_fn(model(hours), marks)

# print(f"w before         : {w_old:.4f}")
# print(f"gradient of w    : {grad_w:.4f}")
# print(f"w - lr * gradient: {w_old - lr * grad_w:.4f}")
# print(f"w after step     : {w_new:.4f}")
# print(f"\nloss before: {loss_before.item():.2f}")
# print(f"loss after : {loss_after.item():.2f}")

# print("\nTakeaway:")
# print("  - optimizer.step() updates weights: w = w - lr * gradient")
# print("  - lr (learning rate) = size of the step.")
# print("  - One step already reduces the loss.")
# print("  - model.parameters() tells the optimizer which weights to update.")


# # =====================================================================
# # DEMO 6 - Why optimizer.zero_grad() is needed
# # =====================================================================
# print("\n========== DEMO 6: optimizer.zero_grad() ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# model = nn.Linear(1, 1)
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# loss_fn(model(hours), marks).backward()
# print("gradient after 1st backward:", round(model.weight.grad.item(), 3))

# loss_fn(model(hours), marks).backward()
# print("gradient after 2nd backward:", round(model.weight.grad.item(), 3), " <- doubled!")

# optimizer.zero_grad()
# print("after zero_grad            :", model.weight.grad)

# loss_fn(model(hours), marks).backward()
# print("gradient after fresh backward:", round(model.weight.grad.item(), 3))

# print("\nTakeaway:")
# print("  - PyTorch ADDS new gradients to old ones.")
# print("  - Without zero_grad(), every step uses wrong (piled up) gradients.")
# print("  - Always call optimizer.zero_grad() before loss.backward().")


# # =====================================================================
# # DEMO 7 - Full training loop
# # =====================================================================
# print("\n========== DEMO 7: Full training loop ==========")

torch.manual_seed(0)
hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

for epoch in range(1000):
    predictions = model(hours)            # 1. predict
    loss = loss_fn(predictions, marks)    # 2. measure error
    optimizer.zero_grad()                 # 3. clear old gradients
    loss.backward()                       # 4. find gradients
    optimizer.step()                      # 5. update w and b

    # if epoch % 200 == 0:
    #     print(f"epoch {epoch:4d} | loss {loss.item():9.4f} | w {model.weight.item():6.2f} | b {model.bias.item():6.2f}")

# print(f"\nlearned: marks = {model.weight.item():.2f} * hours + {model.bias.item():.2f}")
# print("correct: marks = 10.00 * hours + 20.00")


test = model(torch.tensor([20.0]))
print("tesing for input hours: 20")
print(test)

# print("\nTakeaway:")
# print("  - Training = repeat 5 lines: predict, loss, zero_grad, backward, step.")
# print("  - Epoch = one full pass over the data.")
# print("  - Loss goes down, w and b move towards the correct values.")


# # =====================================================================
# # DEMO 8 - Learning rate: too small, good, too big
# # =====================================================================
# print("\n========== DEMO 8: Learning rate ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# for lr in [0.001, 0.05, 0.2]:
#     torch.manual_seed(0)
#     model = nn.Linear(1, 1)
#     loss_fn = nn.MSELoss()
#     optimizer = torch.optim.SGD(model.parameters(), lr=lr)

#     for epoch in range(200):
#         loss = loss_fn(model(hours), marks)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"lr = {lr:<6} -> loss after 200 epochs: {loss.item():.4f} | w {model.weight.item():.2f} | b {model.bias.item():.2f}")

# print("\nTakeaway:")
# print("  - Too small lr -> learns, but very slowly.")
# print("  - Good lr      -> reaches low loss quickly.")
# print("  - Too big lr   -> jumps over the answer, loss explodes (inf / nan).")
# print("  - If loss becomes nan, first thing to try: smaller lr.")


# # =====================================================================
# # DEMO 9 - Optimizers: SGD vs SGD+momentum vs Adam
# # =====================================================================
# print("\n========== DEMO 9: Optimizers ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# optimizers = {
#     "SGD":          lambda params: torch.optim.SGD(params, lr=0.01),
#     "SGD+momentum": lambda params: torch.optim.SGD(params, lr=0.01, momentum=0.9),
#     "Adam":         lambda params: torch.optim.Adam(params, lr=1.0),
# }

# for name, make_optimizer in optimizers.items():
#     torch.manual_seed(0)
#     model = nn.Linear(1, 1)
#     loss_fn = nn.MSELoss()
#     optimizer = make_optimizer(model.parameters())

#     for epoch in range(100):
#         loss = loss_fn(model(hours), marks)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"{name:13s} -> loss after 100 epochs: {loss.item():8.4f} | w {model.weight.item():.2f} | b {model.bias.item():.2f}")

# print("\nTakeaway:")
# print("  - SGD          : w = w - lr * gradient. Simple but slow.")
# print("  - SGD+momentum : keeps moving in the previous direction -> faster.")
# print("  - Adam         : adjusts step size for each weight by itself.")
# print("  - Only ONE line changes between optimizers. Rest of the loop is same.")
# print("  - Each optimizer needs its own good lr (Adam here uses 1.0, SGD 0.01).")
# print("  - Adam is not always the fastest, but it works well with little lr tuning.")
# print("  - So start with Adam. Common lr values: 0.001, 0.01, 0.1")


# # =====================================================================
# # DEMO 10 - Loss functions: MSE vs L1 vs Huber (data with a mistake)
# # =====================================================================
# print("\n========== DEMO 10: Loss functions with an outlier ==========")

# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks_with_mistake = torch.tensor([[30.0], [40.0], [50.0], [60.0], [170.0]])
# print("last mark typed wrong: 170 instead of 70")

# losses = {
#     "MSELoss":   nn.MSELoss(),
#     "L1Loss":    nn.L1Loss(),
#     "HuberLoss": nn.HuberLoss(delta=1.0),
# }

# for name, loss_fn in losses.items():
#     torch.manual_seed(0)
#     model = nn.Linear(1, 1)
#     optimizer = torch.optim.Adam(model.parameters(), lr=1.0)

#     for epoch in range(2000):
#         loss = loss_fn(model(hours), marks_with_mistake)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"{name:10s} -> w {model.weight.item():6.2f} | b {model.bias.item():6.2f}   (correct w 10, b 20)")

# print("\nTakeaway:")
# print("  - MSELoss  : squares errors -> one big mistake pulls the line a lot.")
# print("  - L1Loss   : average of |error| -> not affected much by outliers.")
# print("  - HuberLoss: MSE for small errors, L1 for big ones -> best of both.")
# print("  - Clean data -> MSELoss. Data with outliers -> L1Loss or HuberLoss.")


# # =====================================================================
# # DEMO 11 - Using the trained model (prediction)
# # =====================================================================
# print("\n========== DEMO 11: Prediction ==========")

# torch.manual_seed(0)
# hours = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
# marks = torch.tensor([[30.0], [40.0], [50.0], [60.0], [70.0]])

# model = nn.Linear(1, 1)
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=1.0)

# for epoch in range(500):
#     loss = loss_fn(model(hours), marks)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# model.eval()
# with torch.no_grad():
#     new_hours = torch.tensor([[6.0], [7.5], [0.0]])
#     predicted = model(new_hours)

# for h, p in zip(new_hours.squeeze().tolist(), predicted.squeeze().tolist()):
#     print(f"{h} hours -> {p:.1f} marks")

# with torch.no_grad():
#     single = model(torch.tensor([[8.0]])).item()
# print("single student, 8 hours ->", round(single, 1))

# print("\nTakeaway:")
# print("  - model.eval()        -> switch model to prediction mode.")
# print("  - torch.no_grad()     -> no gradients needed, faster and less memory.")
# print("  - Input shape must match training: (rows, 1) -> [[8.0]] not 8.0")
# print("  - .item() converts a single-value tensor to a Python number.")


# # =====================================================================
# # DEMO 12 - Multiple features and scaling
# # =====================================================================
# print("\n========== DEMO 12: Multiple features + scaling ==========")

# # columns: hours studied, sleep hours  -> marks = 10*hours + 3*sleep + 5
# X = torch.tensor([[1.0, 6.0], [2.0, 8.0], [3.0, 5.0], [4.0, 7.0], [5.0, 8.0]])
# y = torch.tensor([[33.0], [49.0], [50.0], [66.0], [79.0]])

# model = nn.Linear(in_features=2, out_features=1)
# print("2 inputs -> weight shape:", tuple(model.weight.shape), "| bias shape:", tuple(model.bias.shape))
# print("formula: marks = w1 * hours + w2 * sleep + b")

# torch.manual_seed(0)
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.5)
# for epoch in range(2000):
#     loss = loss_fn(model(X), y)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# w1, w2 = model.weight.squeeze().tolist()
# print(f"learned: marks = {w1:.2f} * hours + {w2:.2f} * sleep + {model.bias.item():.2f}")
# print("correct: marks = 10.00 * hours + 3.00 * sleep + 5.00")

# print("\nProblem: features on very different scales")
# # columns: house size in sqft, bedrooms  -> price in lakh
# X_house = torch.tensor([[800.0, 2.0], [1200.0, 3.0], [1500.0, 3.0], [2000.0, 4.0], [2500.0, 4.0]])
# y_house = torch.tensor([[42.0], [62.0], [74.0], [102.0], [122.0]])

# for use_scaling in [False, True]:
#     torch.manual_seed(0)
#     if use_scaling:
#         mean = X_house.mean(dim=0)
#         std = X_house.std(dim=0)
#         X_in = (X_house - mean) / std
#     else:
#         X_in = X_house

#     model = nn.Linear(2, 1)
#     loss_fn = nn.MSELoss()
#     optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

#     for epoch in range(500):
#         loss = loss_fn(model(X_in), y_house)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     label = "with scaling   " if use_scaling else "without scaling"
#     print(f"{label} (same lr = 0.1) -> loss after 500 epochs: {loss.item():.4f}")

# print("\nscaled data (mean 0, std 1 per column):")
# print(((X_house - X_house.mean(dim=0)) / X_house.std(dim=0)).round(decimals=2))

# print("\nTakeaway:")
# print("  - nn.Linear(n, 1) -> one weight per feature + one bias.")
# print("  - Big numbers (sqft ~ 1000s) make gradients huge -> loss explodes.")
# print("  - Scaling: (X - mean) / std  -> every column around 0, similar range.")
# print("  - Use the SAME mean and std later for new data.")


# # =====================================================================
# # DEMO 13 - Train / test split
# # =====================================================================
# print("\n========== DEMO 13: Train / test split ==========")

# torch.manual_seed(0)
# hours = torch.rand(100, 1) * 10
# marks = 10 * hours + 20 + torch.randn(100, 1) * 3

# shuffled = torch.randperm(100)
# train_idx, test_idx = shuffled[:80], shuffled[80:]

# X_train, y_train = hours[train_idx], marks[train_idx]
# X_test, y_test = hours[test_idx], marks[test_idx]
# print("train rows:", len(X_train), "| test rows:", len(X_test))

# model = nn.Linear(1, 1)
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.5)

# for epoch in range(500):
#     model.train()
#     loss = loss_fn(model(X_train), y_train)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# model.eval()
# with torch.no_grad():
#     train_loss = loss_fn(model(X_train), y_train).item()
#     test_loss = loss_fn(model(X_test), y_test).item()
#     test_mae = (model(X_test) - y_test).abs().mean().item()

# print(f"train MSE: {train_loss:.2f}")
# print(f"test  MSE: {test_loss:.2f}")
# print(f"test  MAE: {test_mae:.2f} marks (average mistake per student)")

# print("\nTakeaway:")
# print("  - Train on one part (80%), test on data the model never saw (20%).")
# print("  - Shuffle before splitting so both parts look similar.")
# print("  - Train loss and test loss close -> model generalises well.")
# print("  - With small data, test loss can be a bit lower or higher just by chance.")
# print("  - MAE is easy to explain: 'on average we are off by X marks'.")


# # =====================================================================
# # DEMO 14 - Combined example: house price prediction
# # =====================================================================
# print("\n========== DEMO 14: Combined example - house price ==========")

# # 1. data: sqft, bedrooms, age  ->  price (lakh)
# torch.manual_seed(42)
# n = 200
# sqft = torch.randint(500, 3000, (n, 1)).float()
# bedrooms = torch.randint(1, 5, (n, 1)).float()
# age = torch.randint(0, 30, (n, 1)).float()
# price = 0.04 * sqft + 8 * bedrooms - 0.5 * age + 10 + torch.randn(n, 1) * 3

# X = torch.cat([sqft, bedrooms, age], dim=1)
# y = price
# print("X shape:", X.shape, "| y shape:", y.shape)

# # 2. train / test split
# shuffled = torch.randperm(n)
# train_idx, test_idx = shuffled[:160], shuffled[160:]
# X_train, y_train = X[train_idx], y[train_idx]
# X_test, y_test = X[test_idx], y[test_idx]

# # 3. scaling (mean/std from TRAIN data only)
# mean = X_train.mean(dim=0)
# std = X_train.std(dim=0)
# X_train_s = (X_train - mean) / std
# X_test_s = (X_test - mean) / std

# # 4. model, loss, optimizer
# model = nn.Linear(3, 1)
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.5)

# # 5. training loop
# for epoch in range(600):
#     model.train()
#     predictions = model(X_train_s)
#     loss = loss_fn(predictions, y_train)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     if epoch % 100 == 0:
#         model.eval()
#         with torch.no_grad():
#             test_loss = loss_fn(model(X_test_s), y_test).item()
#         print(f"epoch {epoch:3d} | train MSE {loss.item():9.2f} | test MSE {test_loss:9.2f}")

# # 6. evaluate
# model.eval()
# with torch.no_grad():
#     test_mae = (model(X_test_s) - y_test).abs().mean().item()
# print(f"\ntest MAE: {test_mae:.2f} lakh")

# # 7. predict for new houses
# new_houses = torch.tensor([[1800.0, 3.0, 5.0],
#                            [900.0, 2.0, 20.0]])
# with torch.no_grad():
#     new_prices = model((new_houses - mean) / std)

# for house, p in zip(new_houses.tolist(), new_prices.squeeze().tolist()):
#     print(f"{house[0]:.0f} sqft, {house[1]:.0f} BHK, {house[2]:.0f} yrs old -> {p:.1f} lakh")

# print("\nTakeaway (everything together):")
# print("  1. Data as float tensors, shape (samples, features).")
# print("  2. Shuffle and split into train / test.")
# print("  3. Scale features with train mean and std.")
# print("  4. model = nn.Linear(features, 1), loss = MSELoss, optimizer = Adam.")
# print("  5. Loop: predict -> loss -> zero_grad -> backward -> step.")
# print("  6. Check test loss / MAE on unseen data.")
# print("  7. Predict with model.eval() + torch.no_grad(), same scaling.")
