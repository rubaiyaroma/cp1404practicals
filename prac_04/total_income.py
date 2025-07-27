incomes = []
months = int(input("How many months? "))

# Get incomes
for month in range(months):
    income = float(input(f"Enter income for month {month+1}: "))
    incomes.append(income)

# Print report
print("\nIncome Report")
print("-------------")
total = 0
for month in range(months):
    total += incomes[month]
    print(f"Month {month+1:2} - Income: ${incomes[month]:10.2f} Total: ${total:10.2f}")