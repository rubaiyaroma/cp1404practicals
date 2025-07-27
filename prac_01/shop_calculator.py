# Shop price calculator
print("Shop Calculator")

# Get number of items
while True:
    items = input("Number of items: ")
    if items.isdigit() and int(items) >= 0:
        items = int(items)
        break
    print("Invalid number!")

# Get prices
total = 0
for i in range(items):
    while True:
        price = input(f"Price of item {i+1}: ")
        if price.replace('.', '', 1).isdigit() and float(price) >= 0:
            total += float(price)
            break
        print("Invalid price!")

# Apply discount
if total > 100:
    total *= 0.9

# Show result
print(f"Total for {items} items: ${total:.2f}")