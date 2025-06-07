'''
Prac 3 
James Dixon-Mills

'''

# 1)
# Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

out_file = open("name.txt", "w")
name = input("What is your name? : ")
print(name, file=out_file)
out_file.close

# 2)
# In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close
print(f"Hi {name}!")


