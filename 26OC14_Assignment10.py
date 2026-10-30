import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[:2])
print(arr[2:6])
print(arr[6:], "\n")

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr), "\n")

res= arr*10
print(res, "\n")

print(arr + 10, "\n")
print(arr2 / arr2)
