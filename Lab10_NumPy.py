import numpy as np
import time

# lst = list(range(1_000_000))

# start = time.perf_counter()
# result = [n * 1.18 for n in lst]
# total = time.perf_counter() - start

# print(total)


# array = np.array(lst)
# start = time.perf_counter()
# result = array * 1.18
# total = time.perf_counter() - start

# print(total)

# # array = np.array(lst)

# # print(array)


# array = np.zeros(5)
# print(array)

# array = np.ones(5)
# print(array)

# array = np.eye(4)
# print(array)

# array = np.array([[1, 5, 6], [2, 3, False]])


# print(array)
# print("-" * 50)
# print(array.ndim)
# print("-" * 50)
# print(array.size)
# print("-" * 50)
# print(array.shape)
# print("-" * 50)
# print(array.dtype)

# array = np.array([22,56,89,58])
# slice = array[0:3]  # from 0 till 3 (3 is exclusive)

# print(slice)

# array = np.array([[22,56,89,58],
#                   [90,25,60,84],
#                   [45,71,61,80],
#                   [41,25,61,80]])

# slice = array[1:3, 1:3]  # from 0 till 3 (3 is exclusive)

# print(slice)


# array = np.array([[22,56,89,58],
#                   [90,25,60,84],
#                   [45,71,61,80],
#                   [41,25,61,80]])

# slice = array[array > 50]

# print(slice)


# array = np.array([[22,56,89,58],
#                   [90,25,60,84],
#                   [45,71,61,80],
#                   [41,25,61,80]])

# print(array > 50)


# array = np.array([[22,56,89,58],
#                   [90,25,60,84],
#                   [45,71,61,80],
#                   [41,25,61,80]])
# sum = array.sum()
# min = array.min()
# mean = array.mean()
# print(sum)
# print(min)
# print(mean)


# array = np.array([[22,56,89,58],
#                   [90,25,60,84],
#                   [45,71,61,80],
#                   [41,25,61,80], 
#                   [41,25,61,80]]) 

# #16

# result = array.reshape(-1,6)
# print(result)