### ******Array Matrix********
import numpy as np

arr1 = np.array([
    [1,2,3,4], 
    [5,6,7,8]
])

print("******")
print(arr1.dtype)
##### int32
print("******")
print(arr1.ndim)
#### 2
print("******")
print(arr1.shape)
#### (2, 4) 2 --->> Two rows , 4 --->>> 4 columns
print("******")
print(arr1.size)
#### 8

#### for converting 2D array into 1D array we used .flatten() method

arr2 = arr1.flatten()
print(arr2)
#### [1 2 3 4 5 6 7 8]



