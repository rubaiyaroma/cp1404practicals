from guiter import Guiter

def main():
    print("My guitars!")
    guiters = []

    # Get guiter input
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guiter = Guiter(name, year, cost)
        guiters.append(new_guiter)
        print(f"{new_guiter} added.\n")

    print("\nThese are my guiters:")
    for i, guiter in enumerate(guiters, 1):
        vintage = " (vintage)" if guiter.is_vintage() else ""
        print(f"Guiter {i}: {guiter.name:>20} ({guiter.year}), worth ${guiter.cost:10,.2f}{vintage}")


if __name__ == "__main__":
    main()