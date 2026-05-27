import math
from calculattor import Shap

class Hexagon(Shap):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2

    def get_perimeter(self):
        return 6 * self.side

    def __str__(self):
        return f"Shape: Regular Hexagon"