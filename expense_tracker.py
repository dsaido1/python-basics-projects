expenses = []

expense1 = float(input("Write expense 1: "))
expense2 = float(input("Write expense 2: "))
expense3 = float(input("Write expense 3: "))

expenses.append(expense1)
expenses.append(expense2)
expenses.append(expense3)

total = sum(expenses)

print(expenses)
print("your total expenses is:", total)
print(len(expenses))


