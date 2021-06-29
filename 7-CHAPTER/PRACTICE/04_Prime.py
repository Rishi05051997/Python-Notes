num = int(input("Enter the number: "))
prime = True
for i in range(2, num):
    if(num % i == 0 and  num != 2):
        prime = False
        break
if prime :
    print("This is a prime no")
else :
    print("This is a not a prime no")