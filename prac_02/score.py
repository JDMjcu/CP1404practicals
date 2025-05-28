"""
James Dixon-Mills
CP1404/CP5632 - Practical 1
Broken program to determine score status
"""
score = float(input("Enter score: "))

if score >= 0 and score <= 100:
    if score >= 90:
        print("Excellent Effort")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
else:
    print("Invalid Score")