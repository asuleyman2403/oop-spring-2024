class Animal:
  def __init__(self):
    self.type = 'unknown'
    self.limbs = 4

  def make_sound(self):
    print('Bruuuuh!')
  
class Cat(Animal):
  def __init__(self):
    self.type = 'cat'
    self.limbs = 4
  
  # Методы родительского класса можно переписать дав такое же название
  # Это называется Overriding (или переопределением)
  def make_sound(self):
    print('Meow')

cat = Cat()
cat.make_sound()
