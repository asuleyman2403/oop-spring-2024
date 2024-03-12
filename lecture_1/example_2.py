

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def print(self):
        print(self.brand, self.model)

    def extended_print(self):
        self.print()
        print('Color: ', self.color)


audi = Car("Audi", "Q6", "Black")
toyota = Car("Toyota", "Camry 70", "White")
vaz = Car("Vaz", "Vaz 4", "Blue")

# accessing method outside of the class
audi.print()
toyota.extended_print()
vaz.print()





