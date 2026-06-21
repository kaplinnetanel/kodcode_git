from fastapi import APIRouter
from .animal_dal import Animal_DAL

router = APIRouter()
animals = Animal_DAL()


@router.get("")
def get_animals():
    return animals.get_all_animals()

@router.post("")
def create_animal(name: str, animal_type: str, age: int):
    animals.create_animal(name, animal_type, age)
    return {"message": "Animal Created"}