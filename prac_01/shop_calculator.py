"""
James Dixon-Mills
CP1404 - Practical 1



We Want a result like
Number of items: 3  
Price of item: 100  
Price of item: 35.56  
Price of item: 3.24  
Total price for 3 items is $124.92  

"""

def Calculations(number_of_items):
    Costs = []
    for i in range(number_of_items):
        Costs.append(float(input(f"Whats the price for item {i+1} :")))
         
    for i in range(number_of_items):
        print(f"Price of item {i+1} is $ {Costs[i]}")    
        
    total_cost = sum(Costs)

    if total_cost >= 100:
        Discount = 1/10 * total_cost
        total_cost = total_cost - Discount
        print(f"Your Total bill is $ {total_cost:.2f}")
    else:
        print(f"Your Total bill is $ {total_cost:.2f}")
                   

RUNTIME = True
while RUNTIME == True:
   
    number_of_items = int((input("How Many Items do you have: ")))
    if number_of_items > 0:
        Calculations(number_of_items)
    else:
        print("Invalid number of items!")