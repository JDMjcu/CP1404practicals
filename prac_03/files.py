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

