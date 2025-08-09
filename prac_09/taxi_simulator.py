"""
Cp1404 Prac09
Taxi Simulator task
JDM
Estimate : 45 Minute
Actual: 30 Minutes
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [Taxi("Prius", 100),
         SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]

def main():
    """run taxi simulator program"""
    current_taxi = None
    total_bill = 0
    print("Lets Drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":

        if choice == "c":
            print("Taxis available")
            display_taxis()
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = TAXIS[(taxi_choice)]
                current_taxi.start_fare()
            except IndexError or ValueError:
                print("Invalid taxi choice")
        
            
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    total_bill += fare
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")

        
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis()
    
def display_taxis():
    """Display the list of taxis with their index."""
    for i, taxi in enumerate(TAXIS):
        print(f"{i} - {taxi}")
    
main()