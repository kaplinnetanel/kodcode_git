import math
from shape import Shape

class Hexagon(Shape):
    def __init__(self, shape_id, side):
        super().__init__(shape_id, "hexagon")
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2

    def get_perimeter(self):
        return 6 * self.side

    def __str__(self):
        return f"Shape: Regular Hexagon"
    
    def to_dict(self):
        data = super().to_dict()
        data["side"] = self.side
        return data