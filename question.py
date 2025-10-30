# Question no : 1

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is Negative")

# Question no : 2

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Question no : 3

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# Question no : 4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Larger number is:", a)
else:
    print("Larger number is:", b)

# Question no : 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Question no : 6
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Question no : 7
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# Question no : 8
# Vowel###


# Question no : 9

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# Question no : 10
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# Question no : 11
num = int(input("Enter a number: "))
if 10 <= abs(num) <= 99:
    print("Two-digit number")
else:
    print("Not a two-digit number")

# Question no : 12

char = input("Enter a character: ")
if char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")

# Question no : 13
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
if age >= 18 and weight >= 50:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")


# Question no : 14
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# Question no : 15

units = int(input("Enter number of units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity bill is: Rs.", bill)

# Question no : 16
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Question no : 17
age = int(input("Enter age: "))
if age < 12:
    print("Ticket price: Rs. 100")
elif age <= 18:
    print("Ticket price: Rs. 150")
else:
    print("Ticket price: Rs. 200")

# Question no : 18
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

# Question no : 19
# prime number

