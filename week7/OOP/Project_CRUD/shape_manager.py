import json
import os
from square import Square
from rectangle import Rectangle
from circle import Circle
from hexagon import Hexagon
from triangle import Triangle

class ShapeManager:  
    def __init__(self):
        self.shapes = []              
        self.filename = "shapes.json"  
        self.load_from_json()         

    def create_shape(self, shape_obj):
        self.shapes.append(shape_obj)
        self.save_to_json()

    def get_all_shapes(self): 
        return self.shapes

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return True
        return False

    def update_shape(self, shape_id, key, value):
        for shape in self.shapes:
            if shape.id == shape_id:

                if key == "side" and hasattr(shape, "side"):
                    shape.side = value
                elif key == "width" and hasattr(shape, "width"):
                    shape.width = value
                elif key == "height" and hasattr(shape, "height"):
                    shape.height = value
                elif key == "radius" and hasattr(shape, "radius"):
                    shape.radius = value
                elif key == "base" and hasattr(shape, "base"):
                    shape.base = value
                
                self.save_to_json()
                return True
        return False

    def save_to_json(self):
        dict_list = []
        for shape in self.shapes:
            dict_list.append(shape.to_dict())
            
        with open(self.filename, "w") as file:
            json.dump(dict_list, file, indent=4)

    def load_from_json(self):    
        if not os.path.exists(self.filename):
            return 
            
        with open(self.filename, "r") as file:
            try:
                data_list = json.load(file)
                for item in data_list:
                    t = item["type"]
                    s_id = item["id"]
                    
                    if t == "square":
                        obj = Square(s_id, item["side"])
                    elif t == "rectangle":
                        obj = Rectangle(s_id, item["width"], item["height"])
                    elif t == "circle":
                        obj = Circle(s_id, item["radius"])
                    elif t == "hexagon":
                        obj = Hexagon(s_id, item["side"])
                    elif t == "triangle":
                        obj = Triangle(s_id, item["base"], item["height"], item["side_a"], item["side_b"], item["side_c"])
                    
                    self.shapes.append(obj)
            except json.JSONDecodeError:
                pass