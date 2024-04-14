from .Shape import Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Obdelník Length: {self.length}, Width: {self.width}, Area: {self.area()}"

    def __int__(self):
        return int(self.area())
