"""
James Dixon-Mills
CP1404/CP5632 - Practical 2
program to determine score status
"""
import random

def main():
    """Recieve input and print evaluation."""
    score = float(input("Enter score: "))
    print(evaluate_score(score))

    random_score = random.randint(0,100)
    print(evaluate_score(random_score))


def evaluate_score(score):
    """Seperate the score into 4 evaluations."""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"  


main()