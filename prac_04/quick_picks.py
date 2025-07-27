import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

def main():
    try:
        total_picks = int(input("How many quick picks? "))
        for _ in range(total_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(f"{num:2}" for num in quick_pick))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()