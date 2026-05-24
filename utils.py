from data import solddaier

def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in solddaier:
        if soldier["id"] == soldier_id:
            return soldier
    return None    


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None


def is_valid_status(status: str) -> bool:
    """
    The function checks if the status is valid.
    """

    if status in ("pending","completed","missed"):
        return True
    return False


def is_valid_name(name: str) -> bool:
    """
    The function checks if the soldier's name is valid.
    """
    if name != "":
        return True
    return False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """
    The function checks if a task with this name exists for the specific soldier.
    """
    tasks = soldier["duties"] 
    for task in tasks:
        if task["name"] == duty_name: 
            return True
    return False


def is_valid_day(day: str) -> bool:
    """
    Checks if the day is defined as valid (Sunday to Thursday).
    """
    return day in ("sunday", "monday", "tuesday", "wednesday", "thursday")