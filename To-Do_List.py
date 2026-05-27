def load_tasks(filename):
    new_tasks =[]
    try:
        with open(filename,"r",encoding="UTF8") as f :
            for line in f :
                task =line.strip()
                task =task.split("|")
                new_tasks.append({"id":task[0],"status":task[1],"desc":task[2]})
        return new_tasks        
    except FileNotFoundError:
        return []            

def save_tasks(filename, tasks):
    with open(filename,"w",encoding="UTF-8") as f:
      for task in tasks:
            f.write(f"{task['id']}|{task['status']}|{task['desc']}\n")

def add_task(filename, description) :
    with open(filename,"a",encoding="UTF-8") as f:
        f.write(f"{description}\n")

def complete_task(filename, task_id):
    tasks = load_tasks(filename)
    found = False
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "DONE"  
            found = True
            break    
    if found:
        save_tasks(filename, tasks)  
    else:
        print(f"Error: Task with ID {task_id} not found.")

def list_tasks(filename) :  
    with open(filename,"r",encoding="UTF-8") as f :
        for line in f :
            l =line.strip()
            l = l.split("|")
            if l[1] == "DONE":
                l[1] = "[v]"
            else:
                l[1] = "[]"   
            print(f"{l[1]} {l[0]} | {l[2]}")

def delet_task(filename, task_id):
    tasks = load_tasks(filename)
    keep_tasks = []
    found = False
    for task in tasks:
        if task["id"] != task_id:
            keep_tasks.append(task) 
        else:
            found = True         
    if found:
        save_tasks(filename, keep_tasks) 
        print(f"משימה {task_id} נמחקה בהצלחה!")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def input_choice():
    while True:
        choice = input("תכניס את הבחירה שלך מ 1- 4")
        if  1<= int(choice) <= 4 :
            return str(choice)
                

def main():
    FILENAME = "tasks.txt" 
    while True:
        print('\n=== To-Do List Manager ===')      
        print("הצגת משימות :1")     
        print("הוסף משימה :2")
        print("סמן משימה כהושלמה:3")
        print("יציאה:4")   
        choice = input_choice()
        if choice == "1":      
                list_tasks(FILENAME)
        elif choice == "2":
                desc = input("תיאור מלא של המשימה") 
                add_task(FILENAME, desc)
                print(' המישמה הפסונ !')   
        elif choice == "3":
                task_id = (input("מספר המשימה"))
                complete_task(FILENAME, task_id)      
        elif choice == "4":
                        print("להתראות!")        
                        break      
if __name__ == '__main__': 
      main()  

