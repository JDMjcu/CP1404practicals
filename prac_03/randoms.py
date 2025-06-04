"""
CP1404 - Practical 3
James Dixon-Mills

"""



import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3



# What did you see on line 1? A set of numbers ranging from 5-20 
# What was the smallest number you could have seen, what was the largest? 5 and 20

# What did you see on line 2? 3,5,3,7,3,9
# What was the smallest number you could have seen, what was the largest? 3 and 9 should be odd numbers
# Could line 2 have produced a 4? No, cause 4 is not an odd number 

# What did you see on line 3? 4.077355911500646,
# What was the smallest number you could have seen, what was the largest? smallest 2.5375533070385754, largest  4.1515390891622586, 

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))