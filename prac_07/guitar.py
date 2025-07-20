""" 
Prac-06
Guitar task
Start_Time = 7:41
Estimated time = 60 minutes
Completed First revision of guitar.py @ 7:51
Finsih time = 8:32 
"""



class Guitar():
    """This creates a guitar object"""
    
    def __init__(self, name = '', year = 0, cost = 0.0):
        """Records details of the guitar."""
        self.name = name
        self.year = int(year)         
        self.cost = float(cost)       
    
    def __str__(self):
        """Return a string of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"
    
    
    def get_age(self):
        """Gets the age of the guitar."""
        return 2025 - self.year
    
    def is_vintage(self):
        """Determine if a Guitar is considered vintage."""
        return True if self.get_age() >= 50 else False
    
    def __lt__(self, other_guitar):
        """ Compares two guitars returns true if self is younger than other. """
        return self.year < other_guitar.year
    

