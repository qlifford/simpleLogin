from getpass import getpass

def register():
    while True:
        username = input("> Enter username: ")
        password = getpass("> Create password: ")
        confirm_password = getpass("> Confirm password: ")
        if password == confirm_password:
            password_file = open("pass.txt", "a")
            password_file.write(f"Username: {username}--> Password: {confirm_password}" "\n")
            password_file.close()
            break
        elif password != confirm_password:
            print ("> Passwords don't match: ")
            continue
def login():
    while True:
        username = input("> Enter username: ")
        password = getpass("> Enter password: ")
        password_file = open("pass.txt", "r").read()
        if username and password in password_file:
            print ("Welcome!")
            break
        else:
            print("> Invalid username or password ")
            continue
        password_file.close()
while True:
    reg_or_login = input("Do you want to register or login?: ")
    break
if reg_or_login == "reg":
    register()

elif reg_or_login == "login":
    login()

else:
    print("error")