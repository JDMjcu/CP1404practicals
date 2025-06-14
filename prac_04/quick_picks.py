"""
   James Dixon-Mills
   Prac-04
   
   
    Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
    These values should be stored as CONSTANTS.

    Each line (quick pick) should not contain any repeated number.
    Each line of numbers should be displayed in sorted (ascending) order.
    Study the formatting below so that numbers align neatly.
  
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quickpicks = int(input("How many quickpicks do you want to play? "))

for game in range(number_of_quickpicks):
    quick_pick = []
    for number in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER) 
        while number in quick_pick:
            # Check for number in quickpick if duplicate make a new number
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER) 
        quick_pick.append(number)
        quick_pick.sort()
    print(quick_pick)