# ## ** Accounting system ** ##
# users = {
#     "Ishan": ["8281", 1000],
#     "Prashant": ["1234", 2000]
# }


# def login():
#     while True:
#         print("***- ACCOUNTING SYSTEM -***")
#         username = input("Enter your username: ")
#         pwd = input("Enter your password: ")

#         if username in users and users[username][0] == pwd:
#             print("Login successful")
#             return username  
#         else:
#             print("Invalid password. Try again.")

# def deposit(username):
#     depo = float(input("Enter the amount you want to deposit: "))
#     if depo > 0:
#         users[username][1] += depo
#         print(f"Rs{depo} deposited successfully!")
#     else:
#         print("Invalid deposit amount.")

# def check_balance(username):
#     print(f"Your current balance is Rs{users[username][1]}")


# def withdraw(username):
#     withdraw_amt = float(input("Enter the amount you want to withdraw: "))
#     if withdraw_amt > 0 and withdraw_amt <= users[username][1]:
#         users[username][1] -= withdraw_amt
#         print(f"Rs{withdraw_amt} withdrawn successfully!")
#     else:
#         print("Invalid withdrawal amount or insufficient balance.")

# def main_menu(username):
#     while True:
#         print("\n--- Main Menu ---")
#         print("1. Deposit")
#         print("2. Check Balance")
#         print("3. Withdraw Balance")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             deposit(username)
#         elif choice == "2":
#             check_balance(username)
#         elif choice == "3":
#             withdraw(username)
#         elif choice == "4":
#             print("Thank you for using the Accounting System! 🙏")
#             break
#         else:
#             print("Invalid choice, try again.")



# user = login()
# main_menu(user)





# # Task 2 : Calculator

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y
    

# def calculator():
#     while True:
#         print("\n--- Simple Calculator ---")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")

#         choice = input("Enter choice (1-5): ")

#         if choice == "5":
#             print("Exiting Calculator. Goodbye!")
#             break

#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result:", add(num1, num2))
#         elif choice == "2":
#             print("Result:", subtract(num1, num2))
#         elif choice == "3":
#             print("Result:", multiply(num1, num2))
#         elif choice == "4":
#             print("Result:", divide(num1, num2))
#         else:
#             print("Invalid choice, please try again.")

# calculator()

# task 3: Multiplication table 

# print("----Multiplication Table----")

# while True:
#     num = int(input("Enter the number that is required: "))
#     if num > 0:
#         for i in range(1,11):
#             print(f"{num} X {i}: {num*i}")
#     elif num < 0:
#         print("The number should be positive")
#         continue
#     end=input("Do you want to exit(y/n): ").lower()
#     if end =="y":
#         print("Exit!!")
#         break


# task4: Odd or even
# while True:
#     num = int(input("Enter the number:"))

#     if num > 0 :
#         if num % 2 == 0 :
#             print("It is even")
#         else:
#             print("It is odd")
#         end = input("Do you want to exit:(y/n)")
#         if end== "y":
#             print("Exiting")
#         break
#     elif num < 0:
#         print("Pls input positive number")
        
        

# task 5: palindrome
# def is_palindrome(s):
#     s = s.lower()
#     for i in range(len(s)//2):
#         if s[i] != s[-(i+1)]:
#             print("It is not palindrome")
#             return
        
#     print("It is palindrome")

# word = input("Enter the word: ")

# is_palindrome(word)


# task 6 : login

# print("--Login system--")

# def login():
#     while True:
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if username == "Ishan Shrestha" and password =="1234":
#             print("Your login is successful")
#             break
#         else:
#             print("Try Again!")

# login()


# tsak7: login with registration

# users = {}
# def register():
#     print("--Registration--")
#     username = input("Enter the username:")
#     if username in users:
#         print("Already entered")
#         return
#     password = input("Enter the password: ")
#     users[username]=password    
#     print("Registration Successful!")



# def login():
#     while True:
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if username in users and users[username]==password:
#             print("Your login is successful")
#             break
#         else:
#             print("Try Again!")

# def main():
#     while True:
#         print("--Welcome to Don Club")
#         print("1.Register")
#         print("2.Login")
#         print("3.Exit")
        
#         choice = int(input("Enter which you prefer: "))
#         if choice == 1:
#             register()
#         elif choice == 2:
#             login()
#         elif choice == 3:
#             print("Exiting!!")
#             break
#         else:
#             print("Invalid Try again")
    
# main()

# task 8:print all even number list
# nums = [1,2,3,4,5,6,7,8]

# for num in nums:
#     if num%2==0:
#         print(num)
    


