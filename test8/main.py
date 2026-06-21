import logging
import json
from fastapi import FastAPI, HTTPException

NAME_FILE = "weapons.json"

app = FastAPI()

# הגדרת לוגים - נשמר כפי שכתבת
logging.basicConfig(
    level=logging.DEBUG,
    filename="my_server.log", 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__) # תיקון שם המשתנה (היה loger)

def load_file(name_file):
    with open(name_file, "r", encoding="utf-8") as file:
        return json.load(file)

def dump_file(name_file, data):
    with open(name_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

@app.get("/weapons")
def returns_all_weapons():
    return load_file(NAME_FILE)

@app.get("/weapons/{id}")
def return_weapons_by_id(id: int):
    weapons = load_file(NAME_FILE)
    # שימוש ב-next למציאת פריט בצורה יעילה
    weapon = next((w for w in weapons if w["id"] == id), None)
    if not weapon:
        logger.warning(f"Weapon with id {id} not found")
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon

@app.post("/weapons", status_code=201) # שינוי ל-201 Created
def add_new_weapon(product: dict):
    products = load_file(NAME_FILE)
    # תיקון לוגיקת ה-ID
    new_id = max([w["id"] for w in products], default=0) + 1
    new_product = {
        "id": new_id,
        "type": product.get("type"),
        "model": product.get("model"),
        "ammo_type": product.get("ammo_type"),
        "condition": product.get("condition")
    }
    
    products.append(new_product)
    dump_file(NAME_FILE, products)
    return new_product

@app.delete("/weapons/{id}")
def delete_by_id(id: int):
    products = load_file(NAME_FILE)
    new_weapons = [p for p in products if p["id"] != id]
    
    if len(new_weapons) == len(products):
        raise HTTPException(status_code=404, detail="Item not found")
        
    dump_file(NAME_FILE, new_weapons)
    return {"message": "Deleted successfully"}

# תיקון נתיב ל-Query Parameter
@app.get("/weapons/by-condition")
def get_by_condition(condition: str):
    weapons = load_file(NAME_FILE)
    filtered = [w for w in weapons if w["condition"] == condition]
    if not filtered:
        raise HTTPException(status_code=404, detail="No matching results found.")
    return filtered

@app.get("/weapons/combat-ready")
def get_combat_ready(type: str):
    weapons = load_file(NAME_FILE)
    # תיקון הלוגיקה: condition צריך להיות good או new
    filtered = [w for w in weapons if w["type"] == type and w["condition"] in ["good", "new"]]
    return filtered

@app.get("/weapons/summary/by-type")
def get_summary():
    weapons = load_file(NAME_FILE)
    summary = {}
    for w in weapons:
        w_type = w["type"]
        summary[w_type] = summary.get(w_type, 0) + 1
    return summary
  



