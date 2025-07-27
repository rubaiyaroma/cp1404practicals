numbers = [3, 1, 4, 1, 5, 9, 2]

# Change first to "ten" and last to 1
numbers[0] = "ten"
numbers[-1] = 1

# Print results
print("All numbers except first two:", numbers[2:])
print("Is 9 in numbers?", 9 in numbers)