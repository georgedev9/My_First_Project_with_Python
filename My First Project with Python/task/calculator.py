# Write your code here
print('''
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80 
'''.strip())

prices = [202, 118, 2250, 1680, 1075, 80]

income = sum(prices)

print(f"\nIncome: ${income}")

staff_expenses = int(input("Staff expenses: \n"))

other_expenses = int(input("Other expenses: \n"))

net_income = income - (staff_expenses + other_expenses)

print(f"Net income: ${net_income}")

