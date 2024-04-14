from .Shape import Shape
class RightTriangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Pravouhly trojuhelnik with base {self.base} and height {self.height}, area: {self.area()}"

    def __int__(self):
        return int(self.area())


