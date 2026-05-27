import math
from calculattor import Shap

class Circle(Shap):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius 
    
    def get_area(self): 
        return math.pi * (self.radius ** 2)  
    
    def get_perimeter(self):  
        return 2 * math.pi * self.radius
   
    def __str__(self):    
        return "Shape: Circle"  