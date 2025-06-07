'''
Prac 3 
James Dixon-Mills

'''

# 1)

out_file = open("name.txt", "w")
name = input("What is your name? : ")
print(name, file=out_file)
out_file.close

# 2)

in_file = open("name.txt", "r")
name = in_file.read().strip() # needs the strip otherwise will include a \n
in_file.close
print(f"Hi {name}!")

# 3)

with open("numbers.txt", "r") as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
print(number_one + number_two)    

# 4)

sum_of_numbers = 0
with open("numbers.txt", "r") as in_file:
   for line in in_file:
        number = int(line)
        sum_of_numbers += number
print(sum_of_numbers)