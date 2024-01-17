
class Student:
    def __init__(self, id, name, surname, yearOfStudy, subjects):
        self.name = name
        self.surname = surname
        self.id = id
        self.yearOfStudy = yearOfStudy
        self.subjects = subjects

    def add_subject(self, new_subject):
        self.subjects.append(new_subject)

    def change_year_of_study(self):
        self.yearOfStudy += 1

class Group:
    def __init__(self, discipline):
        self.discipline = discipline
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_info(self):
        print(self.discipline.name)
        for student in self.students:
            print(student.name, student.surname, student.yearOfStudy)


class Discipline:
    def __init__(self, name, class_room, lector):
        self.name = name
        self.class_room = class_room
        self.lector = lector


oop = Discipline("OOP and Data Structures", "A401", "Assyl Suleiman")
students = [
    Student(1, "S1 Name", "S1 Surname", 1, []),
    Student(2, "S2 Name", "S2 Surname", 1, []),
    Student(3, "S3 Name", "S3 Surname", 1, []),
    Student(4, "S4 Name", "S4 Surname", 1, [])
]

group = Group(oop)

for student in students:
    group.add_student(student)

group.print_info()


