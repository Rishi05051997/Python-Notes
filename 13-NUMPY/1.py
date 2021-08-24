import numpy as np

# from array import *

#### ***** Ways Of Creating Array Using Numpy ******
# 1. Using array function on numpy lab
arr = np.array([1,2,3,4,6.0])
# print(arr)
# print(type(arr))
### Output is
### [1. 2. 3. 4. 6.]
### <class 'numpy.ndarray'>

#2. Usinh linspace function on numpy lab
arr2 = np.linspace(0, 15, 16)
# print(arr2)
# print(type(arr2))

### Output is 
### [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
### <class 'numpy.ndarray'>

#3. Using arange function on numpy lab
arr3 = np.arange(1, 15, 1)
# print(arr3)
# print(type(arr3))
## Output is 
## [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
## <class 'numpy.ndarray'>

# i = 0
# mulArr = []
# while i < len(arr3):
#     if i % 2 == 0 and i > 0:
#         for j in range(1, 11):
#             print(j*i)
#     i += 1
    
# 4. Using logspace function on numpy lab
arr4 = np.logspace(1,40,5)
# print(arr4)
### Output is 
## [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30 1.00000000e+40]

# 5. Using Zeros function on numpy lab 
arr5 = np.zeros(5)
# print(arr5)
## [0. 0. 0. 0. 0.]

# 6. Using Ones function numpy lab 
arr6 = np.ones(6)
# print(arr6)
### [1. 1. 1. 1. 1. 1.]
