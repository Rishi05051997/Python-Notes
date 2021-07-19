class Person:
    country = "India"
    
    def __init__(self):
        print("Initializing Person .....\n")

    def takeBreath(self):
        print("Im breathing....")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee .....\n")

    def getSalary(self, salary):
        self.salary = salary
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so Im luckyly breathing....")


class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        # super().__init__()
        print("Initializing Employee .....\n")

    @staticmethod
    def getSalary():
        print(f"No salery to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so Im  breathing++....")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()


pr = Programmer()
# pr.takeBreath()




