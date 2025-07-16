"""
Expected time: 35 Minutes 
Actual time:  28 Minutes
JDM CP1404 
Prac 05  - Email task
"""
def main():
    """ Create dictionary of email to name."""
    email_to_name = {} 
    email = input("Email: ")
    
    while email != "":
        name = get_name_from_email(email)
        
        verification = input(f"Is your name {name}? (Y/n)")
        
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        
        email_to_name[email] = name
        email = input("Email: ")
        
    max_length = max(len(name) for name in email_to_name.values())    
    
    for email, name in email_to_name.items():
        print(f"{name:{max_length}} : {email}")   
        
def get_name_from_email(email):
    """ Exctract a name from the email assuming its firstname.lastname@email """
    identifier = email.split("@")[0]
    names = identifier.split(".")
    fullname = " ".join(names).title()
    return(fullname)


main()    