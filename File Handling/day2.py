# Login and registration system using boths username and password
# To develop the system we will be using dictionary datatype

import json

def register():
    print("-----Register----")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # json.dumps converts dictionary to JSON
    # while converting to string, we can write into the file but we cannot directly convert str to dict so we will be using json
    dict_credential = {username : password}
    json_credential = json.dumps(dict_credential)

    file = open("login.txt","a")
    file.write(json_credential+"\n")
    file.close()

# Login
def login():
    while True:
        print("-----Login----")
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
                if username in dict_credentials and dict_credentials.get(username) == password:
                    print("Login Successful!")
                    return
            
        else: 
            print("Try Again!")


def main():
    
    login()
    
       
main()     