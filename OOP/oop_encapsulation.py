# #1
# class Student:
#     def __init__(self,name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name
# #2
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self): 
#         return self.width * self.height
    
# #3
# class Thermometer:
#     def __init__(self, celsius):
#         self._celsius = celsius 

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value): 
#         if value < -273.15:
#             raise ValueError("ט!")
#         self._celsius = value

# #4

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance    

#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             raise ValueError("י!")
        
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError("אין מספיק כסף בחשבון!")
#         self._balance -= amount     

# #5
# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#     @property    
#     def full_name(self):
#         return f"{self.name} {self.last_name}"   
      
# #6
# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def fahrenheit(self):
#         return (self._celsius * 1.8) + 32

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self._celsius = (value - 32) / 1.8

# #7
# class Calculator:
    
#     @staticmethod 
#     def is_even(n):
#         return n % 2 == 0  
    
# #8
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


#     @classmethod
#     def from_tuple(cls,pair):
#         x , y = pair

#         return cls(x , y)
    
# #9
# class User:
#     count = 0

#     def __init__(self, username):
#         self.username = username
#         User.count += 1
#     @classmethod
#     def how_many(cls):
#         return cls.count 
    

# #10      
# class Product:
#     def __init__(self,price,name):
#         self._name = name 
#         self._price = price

#     @property
#     def name(self):
#         return self._name    

#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price(self,sum):
#         if 0 < sum:
#             self._price = sum
#         raise ValueError("המחיר לא חוקי הוא שלילי")    