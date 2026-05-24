from data import solddaier 
from utils import find_soldier_by_id

def add_soldier(soldier_id: int, name: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier != None :
        raise ValueError(f"כבר קיים במערכת {soldier_id } החייל ")
    if not name or name.strip() == "":
        raise ValueError("שם החייל לא יכול להיות ריק")
    solddaier.append({"name": name, "id": soldier_id, "duties":[]})


def remove_soldier(soldier_id: int) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier == None :
        raise KeyError(f"Soldier with ID {soldier_id} not found in the system.")
    solddaier.remove(soldier)


def get_all_soldiers() -> list:
    return solddaier
    
