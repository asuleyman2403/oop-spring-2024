# Типы наследования
# Гибридное наследование
# В питоне нет понятие интерфейсов, поэтому реализацию нескольких интерфейсов можно достигнуть через гибридное наследование
# Самостояльное можете прочитать что такое интерфейсы в Java (к прим.)

class Vehicle: 
  def move(self): 
    print('method to move vehicle called') 

class Motorcycle(Vehicle): 
  def use_kickstand(self): 
    print('Motorcycle Kickstand') 

class Racing: 
  def go_fast(self): 
    print('method to go fast called') 

  def use_kickstand(self): 
    print('Racing kickstand') 

class RacingMotorcycle(Racing, Motorcycle): 
  def win_cup(self): 
    print('method to win cup called')

class RacingMotorcycle2(Motorcycle, Racing): 
  def win_cup(self): 
    print('method to win cup called')

# Обратите внимание на что два класса отличаются лишь в порядке наследование от родителей
# Порядок наследование имеет значение
moto_1 = RacingMotorcycle()
moto_2 = RacingMotorcycle2()
moto_1.use_kickstand()
moto_2.use_kickstand()

# У подкласса несколько родителей, он перенимает все их свойства

