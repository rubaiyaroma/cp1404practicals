# Get user's name
name = input("Enter name: ")

# Main menu loop
while True:
    # Display menu
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get user choice
    choice = input(">>> ").upper()

    # Process choice
    if choice == "Q":
        break
    elif choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

# Exit message
print("Finished.")