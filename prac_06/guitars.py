""" 
Prac-6 
James Dixon-Mills
start time : 805

"""

from guitar import Guitar

guitars = []

# print("My guitars!")
# name = input("Name: ")
# while name != "":
#     try:
#         year = int(input("Year: "))
#         cost = float(input("Cost: "))
#         guitar = Guitar(name, year, cost)
#         guitars.append(guitar)
#         print(guitar, "added.")
#         name = input("Name: ")       
#     except ValueError:
#         print("Invalid input ")
        
# Sample Guitars
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth ${guitar.cost:10,.2f} {'(vintage)' if guitar.is_vintage() else '' }")