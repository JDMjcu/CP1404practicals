"""
Prac 09 unreliable car task
JDM
"""

from random import randint
from car import Car

class UnreliableCar(Car):
    """An unreliable child of the car class."""
    
    def __init__(self, name, fuel, reliability):
        """Initiialise a unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability
    
    def drive(self, distance):
        """Drive the car sometimes, based off the reliability."""
        random_number = randint(1, 100)
        if self.reliability <= random_number:
            distance = 0
            
        driven_distance = super().drive(distance)
        
        return driven_distance