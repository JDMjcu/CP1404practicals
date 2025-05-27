"""
James Dixon-Mills
CP1404 - Practical 1

"""

## Example Code

# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()


# A)

for i in range(0,110,10):
    print(i, end=" ")
print()    

# B)

# Countdown = 20
# while Countdown > 0:
#     print(Countdown, end=" ")
#     Countdown = Countdown - 1
# print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()


# C)
get_input_c = int(input("Enter a number: "))

for i in range(get_input_c):
    print("*", end='')

# D)
get_input_d = int(input("How many stars: "))

for i in range(1,get_input_d+1):
    print("*" * i)