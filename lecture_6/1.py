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

    def calculate_length(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


rectangle = Rectangle("Rectangle", 4, 5)
print(rectangle.calculate_area(), rectangle.calculate_length())

class Square(Shape):
    def __init__(self, name, a):
        super().__init__(name)
        self.width = a

    def calculate_area(self):
        return self.width ** 2

    def calculate_length(self):
        return self.width * 4

square = Square("Square", 4)
print(square.calculate_area(), square.calculate_length())
