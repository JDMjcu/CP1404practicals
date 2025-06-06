
"""James Dixon-Mills Practical 2"""

MENU = "\n(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Give user a selection of choices in menu."""
    
    score = get_score()
    
    print(MENU)
    user_selection = str(input("Choose an option from above :"))
    
    
    while user_selection != "Q":
        if user_selection == "G":
            score = get_score()

        elif user_selection == "P":
            evaluation = evaluate_score(score)
            print(f"your score is {evaluation}")
                
           
        elif user_selection == "S":
            print('*' * score)
                
            
        print(MENU)
        user_selection = str(input("Choose an option from above :"))
    
    print("goodbye")

def get_score():
    """Get user input for score while checking if its in bounds."""
    score = int(input("Enter a number between 0 and 100: "))
    while  score < 0 or score > 100:
        print("invalid score")
        score = int(input("Enter a number between 0 and 100: "))
    return score

def evaluate_score(score):
    """Seperate the score into 3 evaluations."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"  
      
main()
