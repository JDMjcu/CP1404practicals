"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
You can use the functions min, max, sum and len, and you can use the append method to add a number to a list

"""
# Basic list operations

numbers = []
print("Please enter 5 numbers")
for i in range(5):
    number = int(input(f"Please enter your number {i+1} : "))
    numbers.append(number)
    
print("You entered:", numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")


# Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
            'NicolEye', 'swei45', 'BaseInterpreterInterface', 
            'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 
            'InterpreterInterface', 'StartServer', 'bob'] 

username = input("Please enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access Denied")