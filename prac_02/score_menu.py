def get_score():
    while True:
        score = float(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            return score
        print("Invalid score!")

def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * int(score))

def main():
    score = get_score()

    while True:
        print("\n(G)et new score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "G":
            score = get_score()
        elif choice == "P":
            print(check_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

main()