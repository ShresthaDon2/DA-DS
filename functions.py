# DRY - Dont't Repeat Yourself
# Code resuability => increase
# Code optimization => increase

# def keyword is used to define a function
# Syntax:
# def function_name(parameters):
#   code to be executed

# only by defining the function, the function doesnot work
# To call a function, we use function_name()

# a = 10 
# b = 5
# def addition():  # User defined function
    # print(a+b)
    # return a + b
# return keyword is used to return values 
#  When return keywod returns something, we need a variable to store the returned value

# sum = addition()
# print(sum) 


# Global Variable - The variable that is defined outside the function
# Local Variable - The variable that is defined inside the function 


# Arguments => The value we pass to a function 
# Arguments => There are 2 types of arguments

# Positional arguments (args) => single value arguments

# Keyword Arguments (kwargs) => Arguments those are in key-value pair


# def display(name,age,degree):
#     print("Name= ",name,"Age= ",age,"Degree= ",degree)
#    print(f"Name = {name} Age = {age} Degree = {degree}") 
# display(degree="Engineer",age= 22,name="Ishan")

# f-string

# Lambda Function - Function in one line.

# x= 10 
# y = 2
# def add(x,y):
#     print(x+y)
# add(10,2)

# add = lambda x , y,name: x+y+name

# print(add('10','2',"Ishan"))


#Map - Map function takes a function and a group data type as an argument and perform your condition to each elements
# of the group data type 
# number = [1,2,3,4]

# square = lambda x: x**2

# print(list(map(square,number)))

# filter function
# elements based on a condition
# numbers = [2,3,4,5,6]

# even_numbers= list(filter(lambda x : x%2== 0,numbers))

# print(even_numbers)

# reduce function:
# It also takes function and group data type as an argument and reduces the group datatype elements into a single value acc to our condition
# Combines all elements of a  list  

# import functools
# functools.reduce()

# from functools import reduce

# numbers=[5,6,7,8,9]

# sum = reduce(lambda x,y :x+y,numbers)

# print(sum)

# names = ['Ishan','Don','Shrestha']
# scores = [90,40,50]

# combined = list(zip(names,scores))

# print(combined)

# num1 = [1,2,3,4,5]
# num2= [4,5,6,7,8]
# mixed = list(zip(num1,num2))
# listemp = []
# for i in range(len(num1)):
#     tupleele= tuple((num1[i],num2[i]))
#     listemp.append(tupleele)
# print(listemp)
