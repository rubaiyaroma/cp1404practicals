# 1. Odd numbers (1, 3, 5...19)
print("Odd numbers:")
for num in range(1, 20, 2):
    print(num, end=' ')
print("\n")

# 2. Counting by 10s (0, 10, 20...100)
print("Counting by 10s:")
for num in range(0, 101, 10):
    print(num, end=' ')
print("\n")

# 3. Counting down (20, 19, 18...1)
print("Counting down:")
for num in range(20, 0, -1):
    print(num, end=' ')
print("\n")

# 4. Star line
stars = int(input("How many stars? "))
print("Stars line:")
print("*" * stars)
print()

# 5. Star pyramid
print("Star pyramid:")
for i in range(1, stars+1):
    print("*" * i)