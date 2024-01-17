

class Car:
    # constructor
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def print(self):
        print(self.brand, self.model)

    def extended_print(self):
        # accessing method inside of the class
        self.print()
        print('Color: ', self.color)



audi = Car("Audi", "Q6", "Black")
toyota = Car("Toyota", "Camry 70", "White")
vaz = Car("Vaz", "Vaz 4", "Blue")

# changing object property
audi.color = "White"
print(audi.color)
print(toyota.color)



