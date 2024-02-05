# Магические методы
# Это методы которые исполняются при определенных событиях а не вызываются на прямую
# __init__, __del__ конструктор и деструктор уже являются магическими методами

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
    students_count = 0

    def __init__(self, name, age):
        Student.students_count += 1
        Person.__init__(self, name, age)

    def __del__(self):
        Student.students_count -= 1  

# Вызывается __init__
student = Student("Assyl", 23)

# Вызывается __del__
del student

