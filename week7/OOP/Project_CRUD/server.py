from shape_manager import ShapeManager
from square import Square
from rectangle import Rectangle
from circle import Circle
from hexagon import Hexagon
from triangle import Triangle
from fastapi import FastAPI,HTTPException

manager = ShapeManager()
app =  FastAPI()




@app.get("/shapes")
def all_shapes():
    shapes_objects = manager.get_all_shapes()
    return [shape.to_dict() for shape in shapes_objects]

@app.get("/shapes/count")
def count_shapes():
    shapes_objects = manager.get_all_shapes()
    return len(shapes_objects)


@app.get("/shapes/total-area")
def total_area():
    shapes_objects = manager.get_all_shapes()
    total = 0
    for shape in shapes_objects:
        total += shape.get_area()
    return total    

@app.get("/shapes/{id}")
def shapes_by_id(id :int):
    shapes_objects = manager.get_all_shapes()
    for shape in shapes_objects:
        if shape.to_dict()["id"] == id:
            return shape.to_dict()
    raise HTTPException(status_code=404, detail=f"Shape with id {id} not found")        

@app.post("/shapes", status_code=201)
def create_shape(item: dict):
    shape_type = item.get("type")
    s_id = manager.shapes[-1].id + 1 if manager.shapes else 1
    new_shape = None        
    if shape_type == "square":
        new_shape = Square(s_id, item.get("side"))
    elif shape_type == "rectangle":
        new_shape = Rectangle(s_id, item.get("width"), item.get("height"))
    elif shape_type == "circle":
        new_shape = Circle(s_id, item.get("radius"))
    elif shape_type == "hexagon":
        new_shape = Hexagon(s_id, item.get("side"))
    elif shape_type == "triangle":
        new_shape = Triangle(s_id, item.get("base"), item.get("height"), item.get("side_a"), item.get("side_b"), item.get("side_c"))
    manager.create_shape(new_shape)
    return new_shape.to_dict()

@app.put("/shapes/{id}")
def replace_shapes_data(id: int, data: dict):
    is_updated = False
    for key, value in data.items():
        if manager.update_shape(id, key, value):
            is_updated = True 
    if is_updated:
        return {"mupdated"}
    raise HTTPException(status_code=404, detail="Shape not found or invalid field")

@app.delete("/shapes/{id}")
def delete_shapes(id: int):
   deleted = manager.delete_shape(id)
   if not deleted:
       raise HTTPException(status_code=404)
   return "deleted " 