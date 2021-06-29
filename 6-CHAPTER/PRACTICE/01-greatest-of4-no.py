
num1 = int(input('enter 1 number \n'))
num2 = int(input('enter 2 number \n'))
num3 = int(input('enter 3 number \n'))
num4 = int(input('enter 4 number \n'))

if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3
if(f1 > f2):
    print("The larger no is :",f1)
else:
    print("The larger no is :",f2)
