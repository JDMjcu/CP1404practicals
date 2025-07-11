""" 
Prac-06
Guitar task
Start_Time = 7:41
Estimated time = 60 minutes
Completed First revision of guitar.py @ 7:51
Finsih time = """



class Guitar():
    """This creates a guitar object"""
    
    def __init__(self, name = '', year = 0, cost = 0.0):
        """creates a guitar object with provided details"""
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"
    
    
    def get_age(self):
        return 2025 - self.year
    
    def is_vintage(self):
        return True if self.get_age() >= 50 else False
    
    

     