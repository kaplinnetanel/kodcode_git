from data import solddaier
from solddaier_manager import add_soldier ,remove_soldier,get_all_soldiers
from duty_manager import add_duty_to_soldier,update_duty_status,get_soldier_duties
from utils import find_soldier_by_id,is_valid_name,is_valid_day,is_valid_status,soldier_has_duty

def show_menu() -> None:
    """The function prints the menu for the soldiers"""
    print("""
    ########Main menu for soldier management#######
          
        For selection of soldier management: 
            Adding soldiers: 1
            Removal of soldiers: 2
            View the list of soldiers: 3
          
          *****************************

        For selection to manage the soldiers' missions: 2
            Add task:4
            Mission status update:5
            Viewing the soldier's missions: 6
            Exit the menu : 7

    ###############################################
                  """)

def get_user_choice() -> str:
    """Accepts a choice from the user"""
    while True:
        choice = input("What is your choice from the menu?") 
        if choice in ['1', '2', '3', '4', '5', '6', '7'] and choice != "":
            return choice

def validate_status_input() -> str:
    while True:
        status = input("Enter the status of duty.").strip().lower()
        if is_valid_status(status):
            return status
        print("Invalid status! Please enter pending, completed, or missed.")

def validate_day_input() -> str:
    while True:
        day = input("Enter the soldier's day of duty.").strip().lower() 
        if is_valid_day(day):
            return day
        print("Invalid day! Please enter a day between sunday and thursday.")

def validate_new_id_input() -> int:
    """קלט ID עבור חייל חדש - מוודא שהמספר פנוי"""
    while True:
        try:
            soldier_id = int(input("Enter the soldier's ID."))
            if find_soldier_by_id(soldier_id) is None:
                return soldier_id
            print("Error: This soldier ID already exists in the system!")
        except ValueError:
            print("Error: Please enter numbers only for ID!")

def validate_existing_id_input() -> int:
    """קלט ID עבור חייל קיים - מוודא שהוא אכן נמצא במערכת"""
    while True:
        try:
            soldier_id = int(input("Enter the soldier's ID."))
            if find_soldier_by_id(soldier_id) is not None:
                return soldier_id
            print("Error: Soldier ID not found in the system!")
        except ValueError:
            print("Error: Please enter numbers only for ID!")

def validate_name_input() -> str:
    while True:
        soldier_name = input("Enter the soldier's name.").strip()
        if is_valid_name(soldier_name):
            return soldier_name
        print("Error: Name cannot be empty!")

def handle_add_soldier(soldier_id: int, name: str) -> None:
    try:
        add_soldier(soldier_id, name)
        print(f"Success: Soldier '{name}' with ID {soldier_id} added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def handle_remove_soldier(soldier_id: int) -> None:
    try:
        remove_soldier(soldier_id)
        print(f"Success: Soldier with ID {soldier_id} was removed from the system.")
    except KeyError as e:
        print(f"Error: {e}")

def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()
    if not soldiers:
        print("The system is currently empty. No soldiers registered.")
        return
    print("----------------------------")
    for soldier in soldiers:
        print(f"ID: {soldier['id']} | Name: {soldier['name']}")
    print("---------------------------\n")

def handle_add_duty(soldier_id: int, duty_name: str, day: str) -> None:
    try:
        add_duty_to_soldier(soldier_id, duty_name, day)
        print(f"Success: Duty '{duty_name}' added to soldier {soldier_id} for {day}.")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

def handle_update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    try:
        update_duty_status(soldier_id, duty_name, new_status)
        print(f"Success: Duty '{duty_name}' status updated to '{new_status}'.")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

def handle_view_soldier_duties(soldier_id: int) -> None:
    try:
        duties = get_soldier_duties(soldier_id)
        print(f"\n--- Duties for Soldier ID {soldier_id} ---")
        if not duties:
            print("No duties assigned to this soldier.")
            return
        for duty in duties:
            print(f"duty: {duty['name']} | day: {duty['day']} | status: {duty['status']}")
        print("-------------------------------------------\n")
    except KeyError as e:
        print(f"Error: {e}")

def main() -> None:
    while True:
        show_menu()
        cohice = get_user_choice()

        #אם הוא בוחר שבע אז הוא בעצם עוצר את התוכנית         
        if cohice == "7":
            print("Exiting the system. Goodbye!")
            break
        #בחירה לראות את כל התפריט ולכן שלוש לפני הכל             
        if cohice == "3":
            handle_view_soldiers()
            continue
        #בחירה של אחד מוסיפה לי חיילים אחרי בדיקה והכנסה של השם וid             
        if cohice == "1":
            soldier_id = validate_new_id_input()  
            name = validate_name_input()          
            handle_add_soldier(soldier_id, name)
            continue
            
        if cohice == "2":
        #אם בוחר שתיים אז הוא יכול להסיר חייל             
            soldier_id = validate_existing_id_input()  
            handle_remove_soldier(soldier_id)
            continue
            
        if cohice == "4":
#אם הוא בוחר ארבע אז הוא רוצה להוסיף תורנות             
            soldier_id = validate_existing_id_input()
            duty_name = input("Enter the  duty.").strip() 
            day = validate_day_input()
            handle_add_duty(soldier_id, duty_name, day)
            continue
            
        if cohice == "5":
#אם בוחר חמש מוסיף יום לתורנות             
            soldier_id = validate_existing_id_input()
            duty_name = input("Enter the  duty.").strip()
            status = validate_status_input()
            handle_update_duty_status(soldier_id, duty_name, status)
            continue
            
        if cohice == "6":
#אם בוחר שש אז הוא מראה את התפריט של תורנות של החייל             
            soldier_id = validate_existing_id_input()
            handle_view_soldier_duties(soldier_id)
            continue

if __name__ == "__main__": 
    main()