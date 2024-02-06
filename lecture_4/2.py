# Так поля отличаются при наследовании

class Person:
    def __init__(self, name, age, blood_group, cvv):
        self.name = name
        # Публичное поле
        self.age = age
        # Защищенное поле (протектед)
        self._blood_group = blood_group
        # Приватное поле
        self.__cvv = cvv

    # Getter метод для приватного поле
    def get_cvv(self):
        return self.__cvv

    # Setter метод для приватного поле
    def set_cvv(self, cvv):
        self.__cvv = cvv

    # Setter метод для протектед поле
    def set_blood_group(self, group):
        self._blood_group = group


class Student(Person):
    def __init__(self, name, age, blood_group, cvv, year_of_study, faculty):
        super().__init__(name, age, blood_group, cvv)
        self._year_of_study = year_of_study
        self.faculty = faculty

    def change_cvv(self, cvv):
        # Приватное поле не наследует, поэтому нельзя обратиться через self
        # Поля __cvv записанный в родителе не поменяется
        # Он просто создаст у подкласса новое поле __cvv
        self.__cvv = cvv

    def change_cvv2(self, cvv):
        # Тут все ок, можно поменять поле через setter метод
        self.set_cvv(cvv)

    def change_blood_group(self, group):
        # Протектед поле наследуется, поэтому можно обращаться к полю через self
        self._blood_group = group


student = Student("Assyl", 23, "I", "000", 1, "SDS")
student.change_blood_group("IV")
student.change_cvv("111")
# останется "000"
print(student.get_cvv())

# поменяет на "222"
student.change_cvv2("222")
print(student.get_cvv())

# в Python можно обойти защиту приватного поле таким образом
print(student._Person__cvv)


