'''
Prac 3 
James Dixon-Mills

'''

# 1)
# Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

# out_file = open("name.txt", "w")
# name = input("What is your name? : ")
# print(name, file=out_file)
# out_file.close

# 2)
# In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),

# in_file = open("name.txt", "r")
# name = in_file.read().strip() # needs the strip otherwise will include a \n
# in_file.close
# print(f"Hi {name}!")


# 3)
# Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result

# with open("numbers.txt", "r") as in_file:
#     number_one = int(in_file.readline())
#     number_two = int(in_file.readline())
# print(number_one + number_two)    

# 4)
# Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers.
sum_of_numbers = 0
with open("numbers.txt", "r") as in_file:
   for line in in_file:
        number = int(line)
        sum_of_numbers += number
print(sum_of_numbers)