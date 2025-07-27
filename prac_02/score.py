import random

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # User score
    user_score = float(input("Enter score: "))
    print(get_score_result(user_score))

    # Random score
    random_score = random.randint(0, 120)  # Includes some invalid scores
    print(f"Random score: {random_score} - {get_score_result(random_score)}")

main()