# import numpy as np
from array import *

# arr = np.array([1,2,5,4,8,7,5,8])

# # Method 1: Print values directly (SIMPLEST)
# print("Array elements:", end=" ")
# for value in arr:
#     print(value, end=" ")
# print()  # New line

# # Method 2: Print with indices (if you want positions)
# print("With indices:")
# for i in range(len(arr)):
#     print(f"arr[{i}] = {arr[i]}", end=" ")
# print()

# # Method 3: One-liner (NumPy style)
# print("NumPy way:", " ,".join(map(str, arr)))

# arr = np.append(arr,12)
# # arr = np.insert(arr,12)  this line will not work , because insert require the index at which new value is being added

def printArr(arr):
    for i in arr:
        print(i,end=" ")

# printArr(arr)

nums = array("i",[])

n = int(input("enter the size of the array"))

for i in range(n):
    nums.append(int(input("enter element")))

printArr(nums)
