
"""James Dixon-Mills Practical 2"""

MENU = "\n(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Function docstring"""
    print(MENU)
    user_selection = str(input("Choose an option from above :"))
    
    while user_selection != "Q":
        if user_selection == "G":
            score = get_score()

        elif user_selection == "P":
            print(f"your score is {evaluate_score(score)}")
         
        elif user_selection == "S":
            print_stars(score)
        
        print(MENU)
        user_selection = str(input("Choose an option from above :"))
    
    print("goodbye")

def get_score():
    """gets user input for the score"""
    return float(input("Enter a number: "))

    
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
    
def print_stars(score):
    """Uses the score to make a string of *"""
    for i in range(int(score)):
        print('*', end=' ')
    
    
main()