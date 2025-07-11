""" CP1404- prac 6
    Programming language task
    James Dixon-Mills
"""

class ProgrammingLanguage():
    """Bla bla b;a"""
    
    def __init__(self, name = '', typing = '', reflection = '', year = '0'):
        """Construct a Programming language based of the provided details"""
        self.name = name
        self.reflection = reflection
        self.year = year
        self.typing = typing
        
    def __str__(self):
        return (f"{self.name}, {self.typing} Typing , Reflection = {self.reflection}, First appeared in {self.year}")

        
        
        
        
        
    def is_dynamic(self):
        return self.typing == "Dynamic"
    
    