class Employee:
    company = "TCS"
    salary = 5600
    salaryBonus = 500
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()

print(e.totalSalary)

e.totalSalary = 6000
print(e.salary)