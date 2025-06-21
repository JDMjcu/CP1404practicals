"""
CP1404/CP5632 Practical
Colour to hex code in a dictionary
JDM - 2025

"""


COLOUR_TO_CODE = {"absolute zero": "#0048ba", "amethyst": "#9966cc", "baby pink": "#f4c2c2", "banana yellow": "#ffe135",
                  "generic viridian": "#007f66", "royalblue1": "#4876ff", "ghostwhite": "#f8f8ff", "india green": "#138808",
                  "tomato1": "#ff6347", "sienna2": "#ee7942"}
    
colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except:
        print("Invalid colour")
  
    colour = input("Enter colour: ").lower()
