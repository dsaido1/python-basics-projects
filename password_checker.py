print("Welcome to the password checker")

password = input("Enter your password: ")

length = len(password) >=8
has_number = "0" in password or "1" in password or "2" in password

has_upper = password != password.lower()

if has_number and has_upper and length:
    print("Password is strong")
else :
    print("Password is weak")

