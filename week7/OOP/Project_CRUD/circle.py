import math
from shape import Shape

class Circle(Shape):
    def __init__(self,shape_id, radius):
        super().__init__(shape_id,"circle")
        self.radius = radius 
    
    def get_area(self): 
        return math.pi * (self.radius ** 2)  
    
    def get_perimeter(self):  
        return 2 * math.pi * self.radius
   
    def __str__(self):    
        return "Shape: Circle"  
    
    def to_dict(self):
        data = super().to_dict()
        data["radius"] = self.radius
        return data