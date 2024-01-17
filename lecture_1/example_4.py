class Rectangle:
                # a and b is just arguments
    def __init__(self, a, b):
        self.width = a
        self.length = b

    # first argument is always self
    # encapsulation: getter
    def get_area(self):
        return self.width * self.length
        # return self.a * self.b

# __init__ calls here
rect = Rectangle(4, 5)
area = rect.get_area()
print(area)
