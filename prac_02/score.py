"""
James Dixon-Mills
CP1404/CP5632 - Practical 2
program to determine score status
"""
 
    
"""Module docstring"""

def main():
    """Function docstring"""
    score = float(input("Enter score: "))
    print(evaluate_score(score))


def evaluate_score(score):
    """Function docstring"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"  


main()