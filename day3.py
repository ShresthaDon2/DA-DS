# Constructors
# The special method in oop in python that executes automatically when an object is created
# There is only one constructor and that is __init__
# Constructor always starts and ends with double underscore(__)

# class Student:
#     def __init__(self,name,age,position,roll):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.roll = roll

# s1 = Student("Ishan",22,"Student",5)

        
# print(s1.name)

# Decorators
# Decorators are the special function that takes function 
# as an argumnet and help to modify the original function
# without changing the original function.
# Decorator simply returns the modified version of the function without changing the original function
# We use @ sign as a preffix in a decorator 

# def my_decorator(func):
#     # The decorator always contains a nested function
#     def modify_function():
#         print("Ishan Shrestha")
#         print(22)
#         func()
        
#     return modify_function

# @my_decorator
# def abc():
#     for i in range(5):
#         print(i)

# my_decorator(abc())

# class Student:
#     def __init__(self,name):
#         self.name = name 
    
#     @staticmethod
#     def display():
#         print("Ishannnnn")
        
# s1 = Student("Ishan")
# s1.display()


