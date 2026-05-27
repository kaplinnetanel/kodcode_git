from calculattor import Shap

class Triangle(Shap):
    def __init__(self,base,height ,side_a ,side_b ,side_c):
        super().__init__()
        self.height = height 
        self.base =base
        self.side_a =side_a
        self.side_b = side_b
        self.side_c =side_c

    def get_area(self): 
       return(self.base * self.height) / 2
    
    def get_perimeter(self):  
        return self.side_a + self.side_b + self.side_c     
   
    def __str__(self):    
        return "Shape: Triangle"