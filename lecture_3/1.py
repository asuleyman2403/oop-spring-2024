
class Person:
    def __init__(self, name, age):
        self.name = name

    def get_name(self):
        return self.name

# Пример наследования
class Student(Person):
    def __init__(self, name, age, year_of_study, faculty):
        # Вызов конструктора родителя
        super().__init__(name, age)
        self.year_of_study = year_of_study
        self.faculty = faculty


student = Student("Assyl", 23, 1, "SDS")
# Экземляру класса Student свойственны все неприватные поля и методы класса Person 
print(student.get_name())

