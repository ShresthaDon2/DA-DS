import json
import os
def register():
    print("-----Register----")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # json.dumps converts dictionary to JSON
    # while converting to string, we can write into the file but we cannot directly convert str to dict so we will be using json
    dict_credential = {username: {"password": password, "balance": 0}}
    json_credential = json.dumps(dict_credential)

    file = open("login.txt","a")
    file.write(json_credential+"\n")
    file.close()



# Login
def login():
    print("-----ATM SYSTEM----")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file = open("login.txt","r")
    content = file.read()
    file.close()

    credentials = content.split("\n")
    print(credentials)

# For else:
# for else works same as if else 
# the else block is executed if the break is not encountered in for block
    for i in credentials:
        if i != "":
            dict_credentials = json.loads(i)
            if username in dict_credentials and dict_credentials[username]["password"] == password:
                print("Login Successful!")
                return username
        
    else: 
        print("Try Again!")
        return None

def get_users():
    users = {}
    if os.path.exists("login.txt"):
        with open("login.txt","r") as f:
            for line in f:
                if line.strip():
                    users.update(json.loads(line))
    return users



def save_users(users):
    with open("login.txt","w") as f:
        for u in users:
            f.write(json.dumps({u: users[u]}) + "\n")

def add_balance(username):
    while True:
        users = get_users()
        amount = int(input("Enter the amount you want to deposit: "))
        if amount > 0:
            users[username]["balance"] += amount
            save_users(users)
            print("Amount is deposited")
            break
        else:
            print("Invalid amount!")


def withdraw(username):
    users = get_users()
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount<0:
        print("Invalid amount!")
    elif amount > users[username]["balance"]:
        print("Insufficient amount")
    else:
        users[username]["balance"] -= amount    
        save_users(users)
        print("amount withdrawm!")
            
def check(username):
    users = get_users()
    print(f"Your balance: Rs{users[username]['balance']}")


def main():
    while True:
        print("----ATM----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice:")
        
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("---ATM Menu---")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    c = input("Enter your choice:")

                    if c == "1":
                        check(user)
                    elif c == "2":
                        add_balance(user)
                    elif c == "3":
                        withdraw(user)
                    elif c == "4":
                        print("Logging out!")
                        break
                    else:
                        print("Invalid choice!")
        elif choice =="3":
            print("Thank uou for using!")
            break
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()
                       





