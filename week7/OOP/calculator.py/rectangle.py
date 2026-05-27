from calculattor import Shap

class Rectangle(Shap):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self): 
        return self.width * self.height   
    
    def get_perimeter(self):  
       return 2 * (self.width + self.height)
    
    def __str__(self):    
        return "Shape: Rectangle"