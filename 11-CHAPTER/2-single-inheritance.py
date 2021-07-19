# Single Inheritance
class Employee:
    company = "Google"

    def ShowDetails(self):
        print("This is an employee")


class Programmer(Employee):
    language = "Python"
    company = "YouTube"
    def getLanguage(self):
        print(f"The language is {self.language}")

    def ShowDetails(self):
        print("This is a Programmer")


e = Employee()
e.ShowDetails()
print(e.company)
p = Programmer()
p.ShowDetails()
print(p.company)
