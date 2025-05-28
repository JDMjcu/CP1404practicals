"""
James Dixon-Mills
CP1404 - Practical 2

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Tempreture conversion program """
    
    print(MENU)
    choice = input(">>> ").upper()
    
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celcius: "))
            fahrenheit = convert_celcius_to_farenheit(celsius)
            print(f"{celsius}'C is {fahrenheit:.2f}'F ")
            
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = convert_farenheit_to_celcius(fahrenheit)
            print(f"{fahrenheit}'F is {celcius:.2f}'C ")
        
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celcius_to_farenheit(celsius):
    return celsius * 9.0 / 5 + 32
    
    
def convert_farenheit_to_celcius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)
   
    
main()