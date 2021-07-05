content = True
i = 1
with open('D:\Python-Notes\Python-Notes\9-CHAPTER\PRACTICE\\log.txt') as f:
    
    while content:
        
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line no {i}")
            # print(i)
        i += 1
        