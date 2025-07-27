def main():
    password = get_password()
    print_stars(password)

def get_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Too short!")
        password = input("Password: ")
    return password

def print_stars(password):
    print('*' * len(password))

main()