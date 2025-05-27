"""
James Dixon-Mills
CP1404 - Practical 1


follow sample pseudo code 
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""
get_name = input("What is your name? : ")

MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)
choice = (input("What do you wish to do ? :"))
while choice != "Q":
    if choice == "H":
        print(f"Hello {get_name}")
    elif choice == "G":
        print(f"Farewell {get_name}")
    else:
        print("Invalid Choice")
    print(MENU)    
    choice = (input("What do you wish to do ? :"))
    
if choice == "Q":
    print("Finished")