def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return 5/9 * (fahrenheit - 32)

def main():
    print("C - Celsius to Fahrenheit\nF - Fahrenheit to Celsius\nQ - Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {c_to_f(celsius):.2f}F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {f_to_c(fahrenheit):.2f}C")
        else:
            print("Invalid choice")
        print("C - Celsius to Fahrenheit\nF - Fahrenheit to Celsius\nQ - Quit")
        choice = input(">>> ").upper()
    print("Thanks")

main()