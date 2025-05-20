from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Creating an instance of the Rectangle class
rectangle = Rectangle(5, 10)

# Calling the area method
print("Area:", rectangle.area())  # Output: Area: 50