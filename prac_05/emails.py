"""
Expected time: 35 Minutes 
Actual time:  28 Minutes
JDM CP1404 
Prac 05  - Email task
"""
def main():
    """ Create dictionary of email to name."""
    email_to_name = {} # plan to do something like email : "Name"
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        # make a verification check for either Y or "" as yes and anything else as no
        verification = input(f"Is your name {name}? (Y/n)")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
        
        
    # format the names and email adresses
    for email, name in email_to_name.items():
        print(f"{name:15} : {email}")   
        
def get_name_from_email(email):
    """ Exctract a name from the email assuming its firstname.lastname@email """
    # Treat an email as identifier@email
    identifier = email.split("@")[0]
    names = identifier.split(".")
    fullname = " ".join(names).title()
    return(fullname)


main()    