class Employee:
    salary = 5000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

a = Employee()
a.salaryAfterIncrement = 3000
print(a.salaryAfterIncrement)