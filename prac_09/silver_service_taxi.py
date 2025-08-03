"""
CP1404 Practical 09
SilverServiceTaxi class
JDM

"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.50
    
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
    
    def get_fare(self):
        """Return the fare for the trip including the flagfall."""
        return (super().get_fare() + self.flagfall)

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"