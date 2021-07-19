class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The details of {self.company} employee is {self.name} and product - {self.product}")



vrushabh = Programmer("Vrushabh", "Excell")

Vaibhav = Programmer("Vaibhav", "Powepoint")

vrushabh.getInfo()
Vaibhav.getInfo()


