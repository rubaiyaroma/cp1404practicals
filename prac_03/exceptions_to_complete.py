while True:
    try:
        num = int(input("Enter a number: "))
        break
    except:
        print("Invalid number, try again")

print("Your number is:", num)