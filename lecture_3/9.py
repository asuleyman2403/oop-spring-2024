# Расмотрим пример магического методы __add__

class Employee:
    def __init__(self, name, salary, kpi):
        self.name = name
        self.kpi = kpi
        self.salary = salary

    # Как 1 + 1 = 2 точно также два плохих сотрудника с маленьким зп = один хороший сотрудник с хорошим зп
    # kpi показатель успеваемости сотрудника поэтому оно не может быть больше 1 (100% = 1)
    def __add__(self, other):
        new_emp = Employee('', self.salary + other.salary, min(1, self.kpi + other.kpi))
        return new_emp


emp_1 = Employee("Assyl", 10, 0.2)
emp_2 = Employee("Alibek", 20, 0.3)
emp_3 = emp_1 + emp_2
# '', 30, 0.5
print(emp_3.name, emp_3.salary, emp_3.kpi)

# Есть еще куча методов показаных в слайде
# Можно реализовать логика сравнения, умножения, вычитание для сотрудников и все это достигается с помощью маг. методов


