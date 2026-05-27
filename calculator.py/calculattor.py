
class Shap:  
    def __init__(self): 
        super().__setattr__('is_valid', True)
      
    def get_area(self): 
        pass  
    
    def get_perimeter(self):  
        pass    
   
    def __str__(self):    
        return "Generic Shape"
    
    def __setattr__(self, name, value):
        if name != 'is_valid' and isinstance(value, (int, float)):
            if value <= 0:
                print("Side must be greater than 0") 
                super().__setattr__('is_valid', False)
                raise ValueError("Side must be greater than 0")
        super().__setattr__(name, value)    