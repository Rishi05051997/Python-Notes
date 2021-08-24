#### ****** Creating 3D Array from 2D array ******
import numpy as np

arr1 = np.array([
    [1,2,3,3,4,5,6], 
    [7,8,9,10,11,12], 
     
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2, 4)
print(arr3)