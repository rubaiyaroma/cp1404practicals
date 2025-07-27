import random

starting_price = 10.0
min_price = 1.0
max_price = 100.0
output_file = "prices.txt"

price = starting_price
days = 0
file = open(output_file, 'w')

print(f"Starting price: ${price:.2f}", file=file)

while min_price <= price <= max_price:
    days += 1


    if random.randint(1, 2) == 1:
        price *= 1 + random.uniform(0, 0.175)  # Up 0-17.5%
    else:
        price *= 1 - random.uniform(0, 0.05)  # Down 0-5%


    print(f"Day {days}: ${price:.2f}", file=file)

file.close()