correct_user = "admin"
correct_password = "1234"

username = input("Enter your username: ")
password = input("Enter your password: ")

is_valid = True

if username == correct_user and password == correct_password:
    print("Logged in successfully")
else :
    print("Incorrect username or password")
    is_valid = False