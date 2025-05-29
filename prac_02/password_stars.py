"""
James Dixon-Mills Practical 2 

"""
REQUIRED_LENGTH = 5

def main():
   
    password = get_password(REQUIRED_LENGTH)
    print_stars(password)

def get_password(REQUIRED_LENGTH):
    """Get password, while verify the required length."""
    password = input(str(f"Create a password of atleast {REQUIRED_LENGTH} letters: "))
    while len(password) < REQUIRED_LENGTH:
        password = input(str(f"Your entered password is too small\nCreate a password of atleast {REQUIRED_LENGTH} letters: "))
    
    return password

    
def print_stars(password):
    """Print an amount of stars for length of password."""
    for i in range(len(password)):
        print('*', end=' ')
        
main()