class Number:
    def __init__(self, num):
        self.num = num


    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num
    
    def __truediv__(self, num2):
        print("Lets Division")
        return (self.num / num2.num)

    def __sub__(self, num2):
        print("Lets Substaraction")
        return (self.num - num2.num)


n1 = Number(8)
n2 = Number(8)

sum = n1 + n2
print(sum) 
mul = n1 * n2
print(mul)
div = (n1 / n2)
print(div)
sub = (n1 - n2)
print(sub)