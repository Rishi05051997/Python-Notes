class Person:
    country = "India"
    
    def takeBreath(self):
        print("Im breathing....")


class Employee(Person):
    company = "Honda"

    def getSalary(self, salary):
        self.salary = salary
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so Im luckyly breathing....")


class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No salery to programmers")

    def takeBreath(self):
        print("I am a Programmer so Im  breathing++....")


p = Person()
p.takeBreath()
# print(p.company) # throws an error as Person object not conatine company property
e = Employee()
print(e.company)
e.takeBreath()
e.getSalary(1000)
pr = Programmer()
print(pr.country)
pr.takeBreath()
pr.getSalary()



