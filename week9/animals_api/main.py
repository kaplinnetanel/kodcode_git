from fastapi import FastAPI,HTTPException
from dal.animal_dal import Animal_DAL
from dal.animals_routes import router
import logging

logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

animals = Animal_DAL()

app.include_router(router)

@app.get("/")
def home():
    logger.info("good open home")
    return {"message": "Animals API is running"} 

@app.put("/animals/{animal_id}") 
def update_animal(animal_id,name: str, animal_type: str, age: int ):
    animals.update_animal(animal_id, name, animal_type, age)
    return {"message": "Animal Updated"} 

@app.delete("/animals/{animal_id}")
def delete_animals(animal_id):
    animals.delete_animal(animal_id)
    return {"message": "Animal deleted successfully"}