from abc import ABC, abstractmethod
# ABC = abstract base class


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_length(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

# shape = Shape("Shape")

class Rectangle(Shape):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.width = a
        self.height = b
        self.area = a * b

    def calculate_length(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height

    def __add__(self, other):
        new_rectangle = Rectangle('Huge Rectangle', self.width, self.height + other.height)
        return new_rectangle

    def __str__(self):
        return self.name

    def __int__(self):
        return self.area

rectangle_1 = Rectangle('Rectangle', 4, 5)
rectangle_2 = Rectangle('Rectangle', 5, 6)
huge_rectangle = rectangle_1 + rectangle_2
print(huge_rectangle.width, huge_rectangle.height, huge_rectangle.area)
print(huge_rectangle)
print(int(huge_rectangle))

