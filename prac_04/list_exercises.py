"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
You can use the functions min, max, sum and len, and you can use the append method to add a number to a list

"""
numbers = []
print("Please enter 5 numbers")
for i in range(5):
    number = int(input(f"Please enter your number {i+1} : "))
    numbers.append(number)
    
print("You entered:", numbers)
