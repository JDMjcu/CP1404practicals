"""
CP1404 prac09
Band class 
JDM
Estimated:30 minutes
Actual: 25 minutes
"""

class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician playing their instrument (or not)."""
        return "\n".join(musician.play() for musician in self.musicians)
