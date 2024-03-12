
class Person:
    def __init__(self, name, age):
        self.name = name

    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, age, year_of_study, faculty):
        super().__init__(name, age)
        self.year_of_study = year_of_study
        self.__faculty = faculty

    def set_faculty(self, faculty):
        self.__faculty = faculty
    

student = Student("Assyl", 23, 1, "SDS")
print(student.get_name())

