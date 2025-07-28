"""
James DM 
Cp1404-Prac07
More guitars! exercise
"""
from guitar import Guitar
import csv

def main():
    guitars = []
    
    in_file = open('guitars.csv', 'r', newline='')
    # File format is : Name, Year, Cost
    
    for line in in_file:
        guitar_parts = line.strip().split(',')
        name = guitar_parts[0]
        year = int(guitar_parts[1])
        cost = float(guitar_parts[2])
        guitars.append(Guitar(name, year, cost))
    
    # Close the file as soon as we've finished reading it
    in_file.close()
    
    display_guitars(guitars) 
    
    handle_menu(guitars)

    print("\nFinal list of guitars:")
    display_guitars(guitars)

    out_file = open('guitars.csv', 'w', newline='')
    line = csv.writer(out_file)
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()




def display_guitars(guitars):
    """Sort and loop through and display all guitars."""
    guitars.sort()
    
    for guitar in guitars:
        print(guitar)   
        
def handle_menu(guitars):
    """Asks user if they want to add a guitar to list then does it if wanted."""
    menu = input("Do you wish to add a guitar to the list? y/n ")
    while menu.lower() == "y":
        guitar_name = input("Please enter a guitar name: ")
        guitar_age = input("What year was the guitar made? ")
        guitar_cost = input("How much did it cost? ") 
        
        guitar = Guitar(guitar_name, guitar_age, guitar_cost)   
        guitars.append(guitar)
        menu = input("Do you want to add another guitar to the list y/n")
        
main()