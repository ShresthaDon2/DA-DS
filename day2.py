# Inheritance
# Accessing the properties of parent class by child class

# class Grandparent:
#     name = "Grandparent"
#     def gf(self):
#         print("This is from grandparent class")
        
# class Parent(Grandparent):
#     name = "Parent"
#     def show(self):
#         print("This is from parent class")

# class Child(Parent):
#     name = "Child"
#     def abc(self):
#         print("This is from child class")

# child = Child()
# child.show()
# child.gf()

# Multilevel Inheritance - Hierarchial Inheritance
# Child => Parent => Grandparent
# Child can access the properties of grandparent class directly


# Single Inheritance
# A class inherits from a single parent class 
      
# Multiinheritance 
# A child class inherits from multiple parent class 

# class Animal:
#     def eat(self):
#         print("Animal eats")

# class Dog():
#     def sleep(self):
#         print("Animal sleeps")
        
# class Japenese(Animal,Dog):
#     def barks(self):
#         print("Animal barks")

# d = Japenese()
# d.eat()
# d.sleep()


# Methods overwriting




# To solve the multiple inheritance diamond problem, python has a special technique called MRO

# find the use of mro() method

# class Parent:
#     def abc(self):
#         print("This is parent")

# class Marks:
#     def abc(self):
#         print("This is marks ")


# class get_info(Parent,Marks):
#     pass

# get = get_info()

# get.abc()
# print(get_info.mro())


