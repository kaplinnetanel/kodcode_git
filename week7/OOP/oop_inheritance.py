# #1
# class Animal:
#     def speak(self):
#         return "ewww"

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# #2
# class Vehicle:
#     def describe(self):
#         return "a vehicle"

# class Car(Vehicle):
   
#     pass

# c = Car()
# print(c.describe()) 

# #3
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school

# #4
# class Logger:
#     def log(self, msg):
#         return msg

# class TimeLogger(Logger):
#     def log(self, msg):
#         base_msg = super().log(msg)
#         return f"[time] {base_msg}"
    
# #5    
    
# class Square:
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius ** 2)

# class Triangle:
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height
    
# #6
# class Cat():
#     def speak(self):
#         return "Meow"

# class Duck():
#     def speak(self):
#         return "Quack"

#7
# class Animal:
#     def __init__(self, name):
#         self.name = name 

# class Mammal(Animal):
#     def __init__(self, name, fur_color):
#         super().__init__(name)  
#         self.fur_color = fur_color

# class Dog(Mammal):
#     def __init__(self, name, fur_color, breed):
#         super().__init__(name, fur_color)
#         self.breed = breed  

#8
# def count_dogs(animals):
#     count =0 
#     for a in animals:
#         if isinstance(a , Dog):
#             count += 1
#     return count

# zoo = [
#     Dog("בובו", "חום", "גולדן"),
#     Animal("חיה כלשהי"),
#     Dog("רקס", "שחור", "רוטוויילר"),
#     Mammal("יונק כלשהו", "לבן")
# ] 
# total = count_dogs(zoo)
# print(total)

#9
# class Shape:
#     def __init__(self,side):
#         self.side = side

#     def __str__(self):
#         return f"Shaqe with {self.side}"

# class Square(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def __str__(self):
#         return f"Square {self.radius}"    


# # class Circle(Shape):
# #     def __init__(self):
# #         pass    

# mixed_shapes = [
#     Square(5),
#     Square(10)
# ]
# for shape in mixed_shapes:
#     print(shape)

#10
from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount}=.",end="")


class CardPayment(Payment):
    pass



cash = CashPayment()
cash.pay(100)

card = CardPayment()
card.pay(250)

