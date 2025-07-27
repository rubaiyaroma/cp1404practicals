def get_name_from_email(email):
    front = email.split('@')[0]
    parts = front.split('.')
    name = ' '.join(parts).title()
    return name

email_to_name = {}

email = input("Email: ")
while email != "":
    guessed_name = get_name_from_email(email)
    answer = input(f"Is your name {guessed_name}? (Y/n) ").lower()

    if answer != "y" and answer != "":
        name = input("Name: ")
    else:
        name = guessed_name

    email_to_name[email] = name
    email = input("Email: ")

print()
for email in email_to_name:
    name = email_to_name[email]
    print(f"{name} ({email})")
