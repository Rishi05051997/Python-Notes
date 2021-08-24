def increament(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("THis is not good")

a = increament('sss')
print(a)