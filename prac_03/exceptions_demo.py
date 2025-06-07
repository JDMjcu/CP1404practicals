"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an integer is not entered on either line 10/11
2. When will a ZeroDivisionError occur? When 0 is inputed into the demoninator variable
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Modifying the code to check it before trying to catch it?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")