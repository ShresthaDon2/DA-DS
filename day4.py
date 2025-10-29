# 2. Encapsulation - Hiding secrets in a box

# wraps the data into one unit and hide the inner details
# Attributes and methods 
# # We use __ before the attribute name or method name to hide that data 
# The encapsulated data is hidden from outside the class even its own obj cannot access the hidden data 
# but the hidden data can be accessed from inside the class 
# If we need to access the hidden data , we should create a not hidden attribute or method inside the class in order to access the hidden data 

# class Credential:
#     username = "Ishan"
#     __password= "8281"
    
#     def __reset_password(self,new_password):
#         self.__password = new_password
#         return self.__password
    
#     def abc(self,new_password):
#        password =  self.__reset_password(self,new_password)
#        print(password)
        
# c1 = Credential()
# c1.abc("828144")

#Abstractmethod decorator
# It tells us that every child class inherits the abstract class neds to have the same method 
# as of abstract method

# from abc import ABC, abstractmethod

# class Student(ABC):
    
#     @abstractmethod
#     def course(self):
#         print("Student choosed course...")

# class Ram(Student):
#     def course(self):
#         print("Ram has choosen physics")

    
            
# s1 = Student()
# s1.course()

# r1= Ram()
# r1.course()





