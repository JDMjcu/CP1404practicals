
"""James Dixon-Mills Practical 2"""

MENU = "\n(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Gives user a selection of choices in a menu"""
    print(MENU)
    user_selection = str(input("Choose an option from above :"))
    score = None
    
    while user_selection != "Q":
        if user_selection == "G":
            score = get_score()

        elif user_selection == "P":
            if score != None:
                Evaluation = evaluate_score(score)
                print(f"your score is {Evaluation}")
            else:
                print("Please get a score")
        elif user_selection == "S":
            if score != None:
                # Prints the score as a line of *
                print('*' * score)
            else:
                print("Please get a score")
        print(MENU)
        user_selection = str(input("Choose an option from above :"))
    
    print("goodbye")

def get_score():
    """gets user input for the score"""
    return int(input("Enter a number: "))

    
def evaluate_score(score):
    """Seperates the score into 4 evaluations"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"  
      
main()