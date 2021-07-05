f =  open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\poems.txt', 'r')
data = f.read()
if 'Twinkle' in data:
    print('Twinkle is present')
else:
    print('Twinkle is not present')
# print(data)
f.close()