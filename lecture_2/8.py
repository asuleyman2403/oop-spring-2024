class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


student: Student = Person("Assyl", "Suleiman")


