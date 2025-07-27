import random

# This gives a random whole number between 5 and 20 (including both 5 and 20)
print(random.randint(5, 20))
# Smallest: 5, Largest: 20

# This gives a random number from 3 to 9 (but only odd numbers: 3, 5, 7, 9)
print(random.randrange(3, 10, 2))
# Smallest: 3, Largest: 9
# It cannot be 4 (because of the step of 2)

# This gives a random decimal number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
# Smallest: 2.5, Largest: 5.5

# This gives a random whole number between 1 and 100
print(random.randint(1, 100))