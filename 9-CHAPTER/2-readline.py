
file = open('D:\Python-Notes\Python-Notes\9-CHAPTER\\file.txt', 'r') 
data = file.readline() # readline -->> it reads first line only
print(data)
data = file.readline() # readline -->> it reads secondline only
print(data)
data = file.readline() # readline -->> it reads third line only
print(data)
data = file.readline() # readline -->> it reads fourth line only
print(data)
data = file.readline() # readline -->> it reads fifth line only
print(data)
file.close()