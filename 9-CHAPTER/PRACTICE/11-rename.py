import os

oldname = "D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\oldnname.txt"

newname = "newname_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)

