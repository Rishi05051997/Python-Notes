class Employess:
    company = "Google"
    salary = 100

vrushabh = Employess()
rekha = Employess()

# Creating instance attribute salary for both the objects
vrushabh.salary = 300
# rekha.salary = 500

print(vrushabh.salary)
print(rekha.salary)

# below line throws an error as address is not present in instance/class
# print(rekha.address)
