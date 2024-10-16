correct_user = "admin"
correct_password = "password123"

username = input("enter your username: ")
password = input("enter your password: ")


if username == correct_user and password == correct_password:
    print("access allowed")
else:
    print ("access denied, please try again")