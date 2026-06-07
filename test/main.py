import logging
import json
from fastapi import FastAPI,HTTPException

NAME_FILE = "weapons.json"

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_server.log", 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

loger = logging.getLogger(__name__)

def load_file(name_file):
    """The function downloads the data from the storage file"""
    with open(name_file,"r",encoding="utf-8") as file:
        loger.info("The function was able to successfully open the file and read the data")
        return json.load(file)

def dump_file(name_file,data):
    """The function inserts the data into the file and updates it"""
    with open(name_file,"w",encoding="utf-8") as file:
            json.dump(data,name_file)
            loger.info("The new data was successfully entered into the file")
            return True

@app.get("/weapons")
def returns_all_weapons():
     weapons = load_file(NAME_FILE)
     loger.info("This function brings you the list of all weapons")
     return weapons


@app.get("/weapons/{id}")
def return_weapons_by_id(id:int):
    weapons = load_file(NAME_FILE)
    for weapon in weapons:
        if weapon["id"] == id:
            loger.info("The weapon you were looking for has been successfully found!")
            return weapon
    loger.warning("The weapon you were looking for was not found")    
    raise HTTPException(404,"Weapon not found with the id you provided")       

@app.post("/weapons,{product}",status_code= 202)
def Adding_a_new_product(product: dict):
    """The function adds a new product"""
    products = load_file(NAME_FILE)
    id = len(products) + 1 
    if product.get("type") != None and product.get("model") != None and product.get("ammo_type") != None:
        products.append({"id": id,"type":product["type"] , "model": product[ "model"], "ammo_type": product["mmo_type"], "condition": product["condition"]})
        dump_file(NAME_FILE,products)
        return {"id": id,"type":product["type"] , "model": product[ "model"], "ammo_type": product["mmo_type"], "condition": product["condition"]}
    loger.error("Missing in database")     
    raise HTTPException(400,"Missing in database")





# @app.put("/weapons/{id}{product}")
# def update_existing_weapon(id:int,product:dict):
#       products = load_file(NAME_FILE)
#       for product in products:
#            if product["id"] == id :
#                 products.up
                



@app.delete("/weapons/{id}")
def delet_by_id(id:int):
    new__weapons = []
    products = load_file(NAME_FILE)
    l = len(product)
    for product in products:
           if product["id"] == id :
                loger.info("Item found and deleted")
                continue
           else:    
                new__weapons.append(product)
    if l != len(new__weapons):                
        dump_file(NAME_FILE,new__weapons)
        return True
    raise HTTPException(404,"Item not found")

# @app.get("/weapons/by-condition? condition=")

# @app.get("/weapons/combat-ready?type=")

# @app.get("/weapons/summary/by-type")
# @app.delete("DELETE /weapons/by-condition? condition=")
