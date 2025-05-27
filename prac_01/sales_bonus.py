"""
James Dixon-Mills
CP1404 - Practical 1

Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  

"""
Looping = True
while Looping is True:

    sales = float(input("Enter sales: $"))
    if sales > 0 :
        if sales <= 999:
            bonus = sales/10
            print(f"Your Bonus is {bonus:.2f} ")
        else:
            bonus = 15/100 * sales
            print(f"Your Bonus is {bonus:.2f} ")
    else:
        Looping = False