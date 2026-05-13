List_of_tasks = [
    {"Mission_name": "Buy Grocery", "Priority_level": "High", "done": True},
    {"Mission_name": "Study Python", "Priority_level": "High", "done": False},
    {"Mission_name": "Fix Bug", "Priority_level": "Medium", "done": True},
    {"Mission_name": "Send Mail", "Priority_level": "Low", "done": True},
    {"Mission_name": "Update Git", "Priority_level": "Medium", "done":False}
]

def convert_a_Boolean_value(don : bool)-> str :
    """The function checks whether the task 
    has been completed and converts it to a string."""
    if don : return "completed" 
    return "not completed"

def view_tasks(tasks_list : list ) -> None:
    """The function prints all the tasks for us"""
    for task in tasks_list:
        status = convert_a_Boolean_value(task["done"])
        print(f"----The mission:{task["Mission_name"]}----")
        print(f"----The priority level:{task["Priority_level"]}----")
        print(f"----Was the mission accomplished?:{status}----")
        print("-"*30)

def counting_by_category(task_list : list, category=None, status=None)-> int:    
    """A function that counts by category"""
    if category is None and status == None: return len(task_list)
    counter = 0
    for task in task_list:
        if task[category] == status:
            counter += 1
    return counter

def calculate_how_many_open_tasks(task_list : list)-> int:
    """The function calculates how many open tasks I have."""
    return counting_by_category(task_list,"done",False)


def calculate_how_many_tasks_have_been_completed(task_list:list)-> int:
    """The function calculates for me how many tasks have been completed."""
    return counting_by_category(task_list,"done",True)

def identifier_from_urgent_names(task_list : list)->int:
    """The function identifies urgent tasks."""
    return counting_by_category(task_list,"Priority_level", "High")

def displays_a_dailysummary(task_list : list ,chose):
    """The function shows me a daily summary"""
    print("-"*30)
    if chose == "1":
        print(f"How many tasks are there: {len(task_list)}")
    elif chose == "2":    
        print(f"How many open tasks: {calculate_how_many_open_tasks(task_list)}")
    elif chose == "3":    
        print(f"How many tasks were completed: {calculate_how_many_tasks_have_been_completed(task_list)}")
    elif chose == "4":    
        print(f"Some urgent tasks: {identifier_from_urgent_names(task_list)} ")
    elif chose == "5":
        print(view_tasks(task_list) )    
    print("-"*30)

def displaying_the_menu_and_selecting(task_list,chose):
    """A function that checks your selection"""
    while True:
        if chose not in  "12345":
             chose = input("Choose the option that suits you by number:")
        else:
            break     
    displays_a_dailysummary(task_list,chose)
def main(task_list):
    while True:
        print("How many tasks are there: 1")
        print("How many open tasks: 2")
        print("How many tasks were completed: 3")
        print("Some urgent tasks: 4")
        print("Show all tasks: 5")
        print("Stop the menu.:6")
        chose = input("Choose the option that suits you by number:")
        if chose == "6":
            break
        displaying_the_menu_and_selecting(task_list,chose)

main(List_of_tasks)
