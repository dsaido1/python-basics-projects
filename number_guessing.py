print("welcome to number guessing game")

secret_number = 7

user_number = int(input("Please enter your number: "))


while user_number != secret_number:
    if user_number > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    user_number = int(input("Try again: "))
print("You guessed the number")


