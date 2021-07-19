import math
class Calculator:

    def __init__(self, num):
        self.num = num
    
    def getSquare(self):
        print(f"The square of {self.num} is {self.num**2}")

    def getCube(self):
        print(f"The cube of {self.num} is {self.num**3}")
    
    def getSqaureRoot(self):
        print(f"The square root of {self.num} is {math.sqrt(self.num)}")

    @staticmethod
    def greet():
        print("******Hello there  welcome to the best calculator in the world***********")


number = Calculator(9)

number.greet()
number.getSquare()
number.getCube()
number.getSqaureRoot()
