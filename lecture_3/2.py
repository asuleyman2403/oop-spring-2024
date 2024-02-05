class Person:
    def __init__(self, name, age, cvv, postal_code):
        # Приватные поля не наследуются
        self.__cvv = cvv
        # Наследуются проектед и публичные поля
        self._postal_code = postal_code
        self.name = name
        self.age = age

    def get_postal_code(self):
        return self._postal_code

    def get_cvv(self):
        return self.__cvv


class Student(Person):
    def __init__(self, name, age, year_of_study, faculty, cvv, postal_code):
        super().__init__(name, age, cvv, postal_code)
        self.faculty = faculty
        self.year_of_study = year_of_study

    def print_cvv(self):
        # При попытке прямого обращения будет ошибка
        return self.__cvv


student = Student("Assyl", 24, 3, "SDS", 909, 9000)\
# Тут все ок, метод get_cvv публичный поэтому можно достать cvv через него
print(student.get_cvv())
# Тут будет ошибка
print(student.print_cvv())