
"""James Dixon-Mills Practical 2"""

MENU = "\n(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Give user a selection of choices in menu."""
    print(MENU)
    user_selection = str(input("Choose an option from above :"))
    score = -1
    
    while user_selection != "Q":
        if user_selection == "G":
            score = get_score()

        elif user_selection == "P":
            if score >= 0:
                evaluation = evaluate_score(score)
                print(f"your score is {evaluation}")
            else:
                print("Please get a score")
        elif user_selection == "S":
            if score >= 0:
                # Prints the score as a line of *
                print('*' * score)
            else:
                print("Please get a score")
        print(MENU)
        user_selection = str(input("Choose an option from above :"))
    
    print("goodbye")

def get_score():
    """Get user input for score."""
    return int(input("Enter a number: "))

    
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