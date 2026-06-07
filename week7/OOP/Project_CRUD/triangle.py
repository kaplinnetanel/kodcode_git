from shape import Shape

class Triangle(Shape):
    def __init__(self,shape_id,base,height ,side_a ,side_b ,side_c):
        super().__init__(shape_id,"triangle")
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
    
    def to_dict(self):
        data = super().to_dict()
        data["height"] = self.height
        data["base"] = self.base
        data["side_a"] = self.side_a
        data["side_b"] = self.side_b 
        data["side_c"] = self.side_c 
        return data