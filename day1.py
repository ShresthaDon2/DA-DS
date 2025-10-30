<<<<<<< HEAD
# name="Ishan"
# print(type(name))

# class keyword is used to define a class
# syntax 
# class class_name:
    # Attributes and methods
    
# Attributes - The variable defined inside the class
# methods - the function defined inside the class lower(),upper()

# when creating an object from a class, we need to call a class

# Creating a class

# class Dog:
#     eyes = 2
#     legs = 4
#     def eat(self):
#         print("dog is eating")

# # Creating object from class    
# Tommy = Dog()
# print(Tommy.eyes)

# Seti = Dog()
# print(Seti.legs)
# Seti.eat()

# khairey = Dog()
# khairey.eat()





# class Car:
#     wheels = 4
#     steering = 1
#     door = 4
    
#     def change_info(self,color,brand,name,door): /// Dynamic ///
#         self.color = color
#         self.brand = brand
#         self.name = name 
#         self.door = door 
        
        
# Lambo = Car()
# print(Lambo.door)
# Lambo.change_info("Red","Lambo","3V",2)
# print(Lambo.color)

# Ferari = Car()
# Ferari.change_info("White","Ferarii","16G",7)
# print(Ferari.brand)
# print(Ferari.color)
# print(Ferari.door)

# Object attributes => The attributes that varies depending to the obj 
# Class attributes => The attributes that doesnot varies acc to the obj 



# Task : 
# Create a class student of college"Mindrisers Institution"
# Add class attribute and object attribute

# class Student:
#     college= "Mindrisers Institution"
    
#     def details(self,name,age,address,gender):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.gender = gender
#     def display(self):
#         print(self.name,self.age,self.address,self.gender,self.college)
        
# Ram = Student()
# Ram.details("Ram",22,"raniban","male")
# Ram.display()


=======
# print("Hello world")

 
 
# a = "Ishan Shrestha"

# print(type(a))

# Mutable = data type which obj can be changed

# Non-Mutable = data type which obj cannot be changed but can be changed using different object

# num1 = 10
# num2 = 20 
# print(num1-num2)
# print(num1+num2)
# print(num1*num2)
# print(num1/num2)

# print(num1**num2)
# print(num2%num1)

# print(num1//num2)



# Assignment operators helps to assign value to a variable 

# num1 += 5

# print(num1)

# a = 10
# b = 10

# print(a!=b)


# a = True 
# b = False

# print(a or b)
# print(not b)

# is and not is => is checks the memory location  (identity operators)
# in and not in => in checks whether the value present in group data type or not (Membership operators)

# name = "Ishan Shrestha"
# check = 'a' in name

# print(check)

# name= "ishan shrestha"

# print(name.capitalize())
# print(name.strip())

# list1 = [1,"ishan",2.3,True,[3,3,3,3,3]]

# print(type(list1))


# Calculator

# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))

# operation = input("Enter the operation to be done(+,-,*,/):")

# if operation == "+":
#     print(num1+num2)

# elif operation == "-":
#     print(num1-num2)

# elif operation == "*":
#     print(num1*num2)
    
# elif operation == "/":
#     if num2 == 0:
#         print("0 cannot be divisible")
#     else:
#         print(num1/num2)

# List in mutable data type
# list1= [1,2,3,4,1,5,5,5,5]
# list1.append(7)
# list1.insert(1,9)
# print(list1)

# print(list1.count(1))

# print(list1[3])

# Slicing - Accessing multiple elements or creating a new list from a group data type 
# End_index is exclusive
# print(list1[2:5])

#String data type is also a group data type 

## ** Indexing and slicing in string data type ** ##

# name = "Ishan Shrestha"
# print(name[0:5])

# tuple
# tuple is immutable data type
# tuple1 =(1,2,3,4,"Ishan")

# print(type(tuple1))



# SET {} ==> String doesnot have fix index
# set1 = {1,2,3,3,4,"aanda",2,3,4,9,8}
# set2 = {1,2,3,4,9,8}
# print(set1.intersection(set2))


# Dictionary ==> It is a group data type that has element in key-value pair 
# We also wrap the elements by {}

# dict1 = {"name":"Ishan Shrestha",
#          "age":23,
#          1:2345}

# print(dict1)

# Task: Perform indexing and slicing in all data types like tuple, string, set

# names = ("Ishan","Prashant","Shyam","Gopal","Laxmi")

# print(names[1])
# print(names[0:5])


# drinks = "Fanta and Sprite"

# print(drinks[0])
# print(drinks[0:5])
# print(drinks[6:9])

# name = {1,2,3,4,"Apple","Banana"}
# name2={5,6,7,8,1,2,3,4,"Apple"}

# print(name.intersection(name2))

# print(name.difference(name2))

# dict1 = {
#     "name":"Ishan Shrestha",
#     "age":40,
#     "position":"Data Scientist"
# }
# dict1.update({"sex":"Male"})
# print(type(dict1))

# print(dict1.keys())
# print(dict1.values())
# print(dict1)

# print(dict1.get("name"))
# print(dict1.get("sex"))

# usernames = ["Ishan","Ujjwal","Mary"]
# username = input("Enter your name: ")

# if username in usernames:
#     print("It exist")
# else:
#     print("It doesnot exist")

# dict1 ={
#     "Ishan Shrestha":"ShresthaDon1",
#     "Prashant Shrestha":"ShresthaDon2",
#     "Shyam Shrestha":"ShresthaDon3",
# }
# dict1.update({"Gopal Shrestha": "ShresthaDon4"})
# print(dict1.keys())
# print(dict1.values())
# usernames = dict1.keys()
# username = input("Enter your name: ")
# if username in dict1.keys():
#     print("It exist")
# else:
#     print("It doesnot exist")

# Loops - are used when we need to repeat a same block of code multiple times
# for and while
# for loop is used when we know the start and stop condition
# while loop is used when we don't know the start and stop condition

# Syntax:
# For:

# for iterator in iterable(group data type):
#     Code to be executed 

# Iterator is simply a variable that is used to count the iteration
# Iteration is a single round that is executed when a loop is encountered

# dict1 = {
#     "name":"Ishan Shrestha",
#     "age":40,
#     "position":"Data Scientist"
# }

# for i in dict1:
#     print(dict1.get(i))
# dict1 = "ISHAN"


 
#for i in dict1:
#     print(i)



# list = ["Ishan Shrestha",1,2,3,4]

# for i in list:
#     print(i)
    
# tuple = ("Ishan Shrestha",1,2,3,4)
# for i in tuple:
#     print(i)

# range() => Generates the value: Range takes 3 values => start, end, step 

# for i in range(5,12,2):
#     print(i)


# i = 1
# while i <= 100 :
#     print(i)
#     i += 1


# list = [x**2 for x in range(1,101)]
# use of list comprehension
# we use loop inside the list
# print(list)

# for i in range(9):
#     print(i)
    
# syntax:
#     while condition:
#         code to be executed
# while True:
#     num1 = int(input("Enter a first number: "))
#     num2 = int(input("Enter a second number: "))
#     choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for exit: "))

#     match choice:
#         case 1:
#             print(num1+num2)
#         case 2:
#             print(num1-num2)
#         case 3:
#             print("Exiting")
#             break
#         case _:
#             print("invalid input")
        
# break: BReak cna be used only in loop, when break encounters, it completely exixst the loop 
#continue: continue can be used only in loop, it skips the current iteration but continues the loop 

# list = [x for x in range(1,10)]
# for i in list:
#     if i == 6:
#         print("continue...")
#     continue
#     print(i)

# a = 10 
# b = 9
# c = 6


# if a > b:
#     if a > c:
#         print("a is greatest.")
#     else:
#         print("c is greatest.")
# else:
#     if b > c:
#         print("b is greatest.")
#     else:
#         print("c is greatest")
        
# for i in range(1,6):
#     for j in range(6,11):
#         print(str(i) +","+str(j))
        

# Task :  Make a accounting system where a user
# logins and he should be able to check the balance, add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed.

## // **Accounting system** // ##


users = {
        "Ishan" : ["8281",1000],
        "Prashant" : ["1234",2000]
    }
while True:
    print("---ACCOUNTING SYSTEM---")

    username = input("Enter your username: ")
    pwd = input("Enter the password: ")

    if username in users and users[username][0] == pwd:
        print("login successfull")
        break
    else:
        print("Try again")

while True:
    print("1. Deposit")
    print("2. CHeck the balance")
    print("3. Withdraw balance")
    print("4. Exit")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        depo = float(input("Enter the balnce you want to add: "))
        if depo > 0:
            users[username][1] += depo
            print(f"Rs{depo} is deposited!")
        elif depo < 0:
            print("ENter more amount!")
        else:
            print("Incorrect")
            
    elif choice == 2:
        print(f"Rs{users[username][1]} is the amount you have in your account")
    elif choice == 3:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        users[username][1] -= withdraw
        print(f"Rs{withdraw} is taken out!")
    elif choice == 4:
        print("Thank you for using!!")
        break
    else:
        print("Invalid number")
        
        
# dict1 = {
#     "name":"Ishan",
#     "surname":"Shrestha",
#     "age":22,
#     "position":"Engineer"
# }

# for i in dict1:
#     print(dict1.get(i))
    
    
    
    
    
    
>>>>>>> ab0fefd (Initial commit)
