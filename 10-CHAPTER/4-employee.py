class Employess:
    company = "Google"
    salary = 100

vrushabh = Employess()
rekha = Employess()

vrushabh.salary = 300
rekha.salary = 500

print(vrushabh.company)
print(vrushabh.salary)
print(rekha.company)
print(rekha.salary)

Employess.company = "Youtube"

print(vrushabh.company)
print(rekha.company)

