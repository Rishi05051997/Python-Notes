class Animals:
    animalType = "Mammal"
    pass

class Pets(Animals):
    color = "White"
    pass

class Dogs(Pets):
    
    @staticmethod
    def bark():
        print("The dog is barking")


d = Dogs()

d.bark()