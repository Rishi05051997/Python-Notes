class RailwayForm:
    formType: "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harryApplication = RailwayForm()

harryApplication.name = "Vrushabh"
harryApplication.train = "Rajdhani Express"

harryApplication.printData()
