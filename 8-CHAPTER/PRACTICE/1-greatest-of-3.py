def greatest(num1, num2, num3):
    # if num1 > num3:
    #     f1 = num1
    # else:
    #     f1 = num3
    # if num1 > num2:
    #     f1 = num1
    # else:
    #     f2 = num2
    
    # if f1 > f2 :
    #     return print(f1)
    # else:
    #     return print(f2)
    if(num1 > num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3


a = greatest(1,2,3)
print("The value of the maximum is " + str(a))

b = greatest(56, 99, 55)
print("The value of the maximum is " + str(b))
