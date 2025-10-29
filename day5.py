# Polymorphism => One Action multiple forms 

# => +

# a = 10 
# b = 5 
# print(a+b)

# a = '10'
# b = '5'
# print(a+b)

class Bird:
    name = "Bird"
    
    @staticmethod
    def sound():
        print("Chirping")
        
class Dog:
    name = "Dog"
    def sound(self):
        print("Barking")
        
class Cat:
    name = "Cat"
    def sound(self):
        print("Meowing")
        
b1 = Bird()
d1 = Dog()
c1 = Cat()

print(b1.name)
b1.sound()

print(d1.name)
d1.sound()

print(c1.name)
c1.sound()