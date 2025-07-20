import datetime

class Project():
    """ Represent a project with name, start date, priority, cost estimate, and completion percentage."""
    
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage ):
        """ Initialise a Project instance. """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = float(completion_percentage)
        
    def is_complete(self):
        """ Determine if the project is complete. """
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """ Compares two projects returns true if self is less than other. """
        return self.priority < other.priority
    
    def __str__(self):
        """ Return a string of the guitar."""
        #Example str Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
        return (f"{self.name}, Start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")
    
    
# Test code
    
# project1 = Project("Porject", "12/12/2025", 4, 0, 0.2)
# project2 = Project("This Class", "1/2/2025", 2, 0, 30)
# print(project1)
# print(project1.is_complete())
# print(project1 > project2)