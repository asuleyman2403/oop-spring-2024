# Инкапсуляция это сокрытие данных
# Инкапсуляция = модификаторы доступа + getter + setter

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


person = Person("Assyl", 23, "I", "000")
# Публичные поля не защищены вообще, поэтому их можно менять и обращаться напрямую
person.name = "Arman"
person.age = 24
print(person.name, person.age)

# К протектед полю можно обращаться напрямую
# Но менять лучше стоит через setter метод
# Есть прямой доступ поэтому getter можно не реализовывать
print(person._blood_group)
person.set_blood_group("II")

# Приватному поле нельзя обращаться извне, только внутри класса
# 41 вызовет ошибку
# print(person.__cvv)
# Так как нет прямого доступа нужно пользоваться getter/setter методами
person.set_cvv("999")
print(person.get_cvv())

# field_name = public
# _field_name = protected
# __field_name = private

