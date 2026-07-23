num1 = int(input("first number: "))
num2 = int(input("second number: "))

operation = input("choose one of those *+-/ ")

if operation == "*":
   result = num1 * num2
   print(result)
elif operation == "+":
   result = num1 + num2
   print(result)
elif operation == "-":
   result = num1 - num2
   print(result)
elif operation == "/":
   result =num1 / num2
   print(result)
else: print("invalid operation")