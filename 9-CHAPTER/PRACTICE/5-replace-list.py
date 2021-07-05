words = ["donky", "kaddu", "mote"]

with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\sample.txt') as f:
        a= f.read()


for word in words:
    a = a.replace(word, "#2@GG@@@")

    with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\sample.txt', 'w') as f:
        f.write(a)