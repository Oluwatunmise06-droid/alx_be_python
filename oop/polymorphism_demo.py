import math

class Shape:
    def area(self):
        """Base method for calculating area. 
        Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of a circle"""
        return math.pi * (self.radius ** 2)
