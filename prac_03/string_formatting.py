# Example of using string formatting with .format() and f-strings
name = "Gibson L-5 CES"
year = 1922
cost = 16035.50

print(f"{year} {name} for about ${cost:.0f}!")

# Print powers of 2 using a loop
for i in range(11):
    print(f"2 ^ {i} is {2 ** i}")