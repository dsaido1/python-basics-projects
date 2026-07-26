def calculator():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))

    operation = input("choose one of those *+-/ ")

    if operation == "*":
        result = num1 * num2

    elif operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"
    return result

answer = calculator()
print(answer)
