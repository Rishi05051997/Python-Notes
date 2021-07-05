file1  = "D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\copy.txt"

file2 = "D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")