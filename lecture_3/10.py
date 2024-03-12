class Car:
    def make_sound(self):
        print('Broom')

class Animal:
    def make_sound(self):
        print('AAA')

class Cow(Animal):
    def make_sound(self):
        print('Mooo')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

sound_makers = [Car(), Cat(), Cow()]
for item in sound_makers:
    item.make_sound() 
