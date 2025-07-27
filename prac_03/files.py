# Part 1: Ask the user for their name and save it to a file
name = input("Enter your name:")
file = open("name.txt", "w")
file.write(name)
file.close()

# Part 2: Read the name from the file and greet the user
file = open("name.txt", "r")
name = file.read()
file.close()
print("Hi " + name + "!")

# Part 3: Read first two numbers from numbers.txt and add them
file = open("numbers.txt","r")
num1 = int(file.readline())
num2 = int(file.readline())
file.close()
print("First two numbers added:", num1 + num2)

# Part 4: Add all numbers in numbers.txt
file = open("numbers.txt","r")
total = 0
for line in file:
    total += int(line)
file.close()
print("Total of all numbers:", total)