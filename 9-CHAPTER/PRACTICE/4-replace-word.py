with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\dummy.txt') as f:
    a = f.read()
a = a.replace("donky", "#2@GG@@@")

with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\dummy.txt', 'w') as f:
    f.write(a)

