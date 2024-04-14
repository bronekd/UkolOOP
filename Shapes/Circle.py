import math
from .Shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return f"Kruh s poloměrem {self.radius}, má plochu {self.area()}"

    def __int__(self):
        return int(self.area())