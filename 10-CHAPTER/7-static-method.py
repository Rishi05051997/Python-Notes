class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

vrushabh = Employee()

vrushabh.salary = 10000

vrushabh.getSalary("Thanks!") # Employee.getSalary(vrushabh)

vrushabh.greet() # Employee.greet()

vrushabh.time()