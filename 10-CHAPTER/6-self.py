class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

vrushabh = Employee()

vrushabh.salary = 10000

vrushabh.getSalary() # Employee.getSalary(vrushabh)
