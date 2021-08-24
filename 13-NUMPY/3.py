#### Copying Array in python
import numpy as np

arr = np.array([1,2,3,4,5])
arr1 = arr + 6

# print(arr1)
##### [ 7  8  9 10 11]

arr2 = np.array([1,2,3,4,5])
arr3 = np.array([6,7,8,9,10])
arr5 = arr2 + arr3
print(arr5)
##### [ 7  9 11 13 15]


