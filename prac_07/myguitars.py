from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    """Read guitars from file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # skip bad lines
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(filename, guitars):
    """Save the list of Guitar objects to file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    """Display a numbered list of guitars."""
    print("Guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")

def main():
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    print("\nSorted by year (oldest to newest):")
    guitars.sort()
    display_guitars(guitars)

    # Add new guitars
    print("\nAdd new guitars (enter a blank name to stop):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    # Sort and save to file
    guitars.sort()
    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")
    print("Final list:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()