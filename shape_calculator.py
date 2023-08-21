import math

class Rectangle:
    def __str__(self):
        return f"Rectangle(width={self.w}, height={self.h})"
    def set_width(self, width):
        self.w = width
    def set_height(self, height):
        self.h = height
    def get_area(self):
        return self.h * self.w
    def get_perimeter(self):
        return self.h * 2 + self.w * 2 
    def get_diagonal(self):
        return (self.h ** 2 + self.w **2) ** .5
    def get_picture(self):
        if self.w > 50 or self.h > 50:
            return "Too big for picture."
        return f"{'*' * self.w}\n" * self.h
    def get_amount_inside(self, shape):
        if self.w < shape.w or self.h < shape.h: return 0
        else: return int(self.w/shape.w) * int(self.h/shape.h)
    def __init__(self, width, height):
        self.w = width
        self.h = height

class Square(Rectangle):
    def set_side(self, side):
        self.w = side
        self.h = side
    def __str__(self):
        return f"Square(side={self.w})"
    def __init__(self, side):
        self.w = side; self.h = side
