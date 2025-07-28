""" CP1404- prac 6
    Programming language task
    James Dixon-Mills
"""

class ProgrammingLanguage():
    """Represent programing languages as objects"""
    
    def __init__(self, name = '', typing = '', reflection = '', year = '0'):
        """Construct a Programming language based of the provided details"""
        self.name = name
        self.reflection = reflection
        self.year = year
        self.typing = typing
        
    def __str__(self):
        """Return a string for the language."""
        return (f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}")

    def is_dynamic(self):
        """Determine if the language is Dynamic."""
        return self.typing == "Dynamic"