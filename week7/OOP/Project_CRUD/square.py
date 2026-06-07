from shape import Shape

class Square(Shape):
    def __init__(self, shape_id, side):
        super().__init__(shape_id, "square")
        self.side = side
    
    def get_area(self):
        return self.side * self.side
        
    def get_perimeter(self):
        return 4 * self.side
    
    def __str__(self):    
        return "Shape: Square"
    
    def to_dict(self):
        data = super().to_dict()
        data["side"] = self.side
        return data