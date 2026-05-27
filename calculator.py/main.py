from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle
def main():
    shapes = [
        Rectangle(10, 5),
        Square(4),
        Triangle(6, 4, 5, 6, 5),
        Circle(3),
        Hexagon(5)
    ]
    
    for shape in shapes:
        print(shape)  
        print(f"Area: {shape.get_area():.2f}")
        print(f"Perimeter: {shape.get_perimeter():.2f}")
        print("-" * 20)  

if __name__ == "__main__":
    main()