"""
James Dixon-Mills Practical 2 

"""

REQUIRED_LENGTH = 5

password = input(str(f"Create a password of atleast {REQUIRED_LENGTH} letters: "))

while len(password) < REQUIRED_LENGTH:
    password = input(str(f"Your entered password is too small\nCreate a password of atleast {REQUIRED_LENGTH} letters: "))

for i in range(len(password)):
    print('*', end=' ')