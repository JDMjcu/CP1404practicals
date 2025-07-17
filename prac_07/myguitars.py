"""
James DM 
Cp1404-Prac07
More guitars! exercise
"""
from guitar import Guitar
import csv

def main():
    guitars = []
    
    in_file = open('guitars.csv', 'r')
    # File format is : Name, Year, Cost
    for line in in_file:
        # print(repr(line))  # debugging
        guitar_parts = line.strip().split(',')
        guitar_object = Guitar(guitar_parts[0],guitar_parts[1],guitar_parts[2])
        
        guitars.append(guitar_object)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)
    
    guitars.sort()
    
    for guitar in guitars:
        print(guitar)    
    
main()