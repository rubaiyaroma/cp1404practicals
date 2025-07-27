CODE_TO_NAME = {
    "QLD":"Queensland",
    "NSW":"New South Wales",
    "NT":"Northern Territory",
    "WA":"Western Australia",
    "ACT":"Australian Capital Territory",
    "VIC":"Victoria",
    "TAS":"Tasmania",
    "SA":"South Australia"
}

print("State abbreviations and names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:>3} is {name}")

print()

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code} is {state_name}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
