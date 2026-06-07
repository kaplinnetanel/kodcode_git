from shape_manager import ShapeManager
from square import Square
from rectangle import Rectangle
from circle import Circle
from hexagon import Hexagon
from triangle import Triangle

def menu_display():
    print("-" * 40)
    print("1. Add shape\n2. Show all shapes\n3. Update shape\n4. Delete shape\n5. Exit")
    print("-" * 40)

def main():
    manager = ShapeManager()
    
    while True:
        menu_display()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            t = input("1.Square, 2.Rectangle, 3.Circle, 4.Hexagon, 5.Triangle: ")
            next_id = manager.shapes[-1].id + 1 if manager.shapes else 1
            
            if t == "1": manager.create_shape(Square(next_id, float(input("Side: "))))
            elif t == "2": manager.create_shape(Rectangle(next_id, float(input("Width: ")), float(input("Height: "))))
            elif t == "3": manager.create_shape(Circle(next_id, float(input("Radius: "))))
            elif t == "4": manager.create_shape(Hexagon(next_id, float(input("Side: "))))
            elif t == "5": manager.create_shape(Triangle(next_id, float(input("Base: ")), float(input("Height: ")), float(input("A: ")), float(input("B: ")), float(input("C: "))))
            print("Successfully added!")

        elif choice == "2":
            for s in manager.get_all_shapes():
                print(f"ID: {s.id} | {s} | Area: {s.get_area():.2f} | Perimeter: {s.get_perimeter():.2f}")

        elif choice == "3":
            s_id = int(input("Enter ID to update: "))
            key = input("Property to update (side/width/height/radius/base): ")
            val = float(input(f"Enter new value: "))

            if manager.update_shape(s_id, key, val): print("Updated!")
            else: print("ID not found.")

        elif choice == "4":
            if manager.delete_shape(int(input("Enter ID to delete: "))): print("Deleted!")
            else: print("ID not found.")

        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()