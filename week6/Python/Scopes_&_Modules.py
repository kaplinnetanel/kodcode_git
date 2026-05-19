#1
# count = 0 
# def bump():
#     global count 
#     count += 1

# def value() :
#     return count

# bump()
# bump()
# bump()
# print(value())

#2
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter    

# c = make_counter()
# print(c())  # מדפיס: 1
# print(c())  # מדפיס: 2
# print(c())
#3
# x = "global"
# def outer(): 
#     x = "enclosing" 
#     def inner(): 
#         x = "local" 
#         print(x) 
#     inner() 
#     print(x)
# outer()
# print(x)

#4
# l = [1, 2, 3] 
# print(list(range(5)))

#5
# from Mathutils import square
# import Mathutils 
# print(square(3)) 
# print(Mathutils.cube(3))

#6
# import tools
# print(tools.add(10, 10))

#7
# import datetime
# current_time = datetime.datetime.now()
# print(current_time)

#8
# import math
# def public_names(m):
#     public_list = [name for name in dir(m) if not name.startswith('_')]
#     return sorted(public_list)

# print(public_names(math))

#9
def add_item(item, bag=[]):
    if bag == []:
        bag = [] 
    bag.append(item) 
    return bag
print(add_item("r"))
print(add_item("r"))