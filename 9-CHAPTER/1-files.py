# Use open function to read the content of a file
file = open('D:\Python-Notes\Python-Notes\9-CHAPTER\\file.txt', 'r') # by default the mode is read
# data = file.read()
data = file.read(5) # reads first 5 characters from the file
print(data)
file.close()
