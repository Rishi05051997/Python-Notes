class Employee:
    company = "Camel"

    salary = 1000
    location = "Delhi"

    @classmethod
    def changeSalry(cls, sal):
        # self.__class__.salary = sal
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalry(500)
print(Employee.salary)

