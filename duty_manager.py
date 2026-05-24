
from data import solddaier
from utils import find_soldier_by_id, soldier_has_duty, is_valid_day, is_valid_status

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """The function adds a duty to the soldier after a comprehensive check"""
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError("אם חייל עם id זה לא נמצא במערכת")
    
    if soldier_has_duty(soldier, duty_name):
        raise ValueError("תורנות עם שם זה כבר קיימת לחייל")
        
    if not is_valid_day(day):
        raise ValueError("אם day לא חוקי (friday/saturday או ערך לא תקין")
    
    soldier["duties"].append({"name": duty_name, "day": day, "status": "pending"})


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    The function updates a duty status to a soldier after validating inputs.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError("אם חייל עם id זה לא נמצא במערכת")
        
    if not is_valid_status(new_status):
        raise ValueError("אם new_status לא חוקי (לא pending/completed/missed)")
        
    if not soldier_has_duty(soldier, duty_name):
        raise KeyError("אם תורנות עם שם זה לא נמצאה לחייל")
        
    for task in soldier["duties"]:
        if task["name"] == duty_name:
            task["status"] = new_status
            break


def get_soldier_duties(soldier_id: int) -> list:
    """
    The function returns the list of duties for a specific soldier.
    """
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
        
    return soldier["duties"]