MIN_LENGTH = 5
MAX_LENGTH = 15
NEEDS_SPECIAL = True
SPECIALS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print("Create a password with:")
    print(f" {MIN_LENGTH} to {MAX_LENGTH} characters")
    print(" At least 1 uppercase letter")
    print(" At least 1 lowercase letter")
    print(" At least 1 number")
    if NEEDS_SPECIAL:
        print(" At least 1 special character")

    while True:
        password = input("Your password: ")
        if check_password(password):
            print(f"Great! Your {len(password)} character password works.")
            break
        else:
            print("Please try again.")

def check_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    has_upper = has_lower = has_number = has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif NEEDS_SPECIAL and char in SPECIALS:
            has_special = True

    if not (has_upper and has_lower and has_number):
        return False
    if NEEDS_SPECIAL and not has_special:
        return False
    return True
main()
