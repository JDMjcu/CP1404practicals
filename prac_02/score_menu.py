'''display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>'''


"""James Dixon-Mills Practical 2"""

MENU = "(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Function docstring"""
    print(MENU)
    user_selection = input(str("Choose an option from above :"))
    
    while user_selection != "Q":
        if user_selection == "G":
            score = get_score()

        elif user_selection == "P":
            if score == None:
                print("Please get a score")
            print(evaluate_score(score))
        
        print(MENU)
        user_selection = input(str("Choose an option from above :"))


def get_score():
    """Function docstring"""
    return int(input("Please Choose a number from 0 - 100 : ")) 
    
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