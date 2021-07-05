with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\this.txt') as f:
    content = f.read()

with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\copy.txt', "w") as f:
    f.write(content)