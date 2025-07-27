print("Let's divide two numbers!")

try:
    top = int(input("Enter first number (numerator): "))
    bottom = int(input("Enter second number (denominator): "))

    if bottom == 0: # get number from user
        print("Oops! You can't divide by zero.")
    else:
        answer = top / bottom
        print(f"The answer is {answer}")

except ValueError:  # If user doesn't enter a proper number
    print("Please only enter whole numbers (no decimals or text)")

print("All done!")