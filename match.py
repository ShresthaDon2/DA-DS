# match is similar to the switch case in C.
# match keyboard is used to define a matching condition and case keyword is used to check the matching value
a = 10
b = 20
choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: "))

match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid Input!")
        choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: "))

# Task: update calculator task using match keyword

#Task: Find the Day name from the Day number

a = 10 
match a:
    case 10 | 20:
        print("It's macthday")
        
        