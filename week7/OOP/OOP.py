# #3
# class Counter:
#     def __init__(self, start=0):
#         self.count = start
#     def increment(self):
#         self.count += 1

#     def value(self):
#         return self.count

# #4

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x},frf {self.y})"
    
# #5
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Transaction rejected: Insufficient funds.")
#         elif amount <= 0:
#             print("Withdrawal amount must be positive.")
#         else:
#             self.balance -= amount

# #6           
# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def to_fahrenheit(self):
#         return (self.celsius * 9 / 5) + 32
# #7
# class Student:
#     school = "Kodcode"
#     def __init__(self, name):
#         self.name = name

# f = Student("alise")
# print( f.name , f.school)

#8
# class Player:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Player.count += 1

# #9
# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def is_more_than(self, other):
#         return self.amount > other.amount
