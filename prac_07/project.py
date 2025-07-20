import datetime

class Project():
    """ Represent a project with name, start date, priority, cost estimate, and completion percentage."""
    
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage ):
        """ Initialise a Project instance. """
        self.name = name
        # self.start_date = start_date Do after everything else
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = float(completion_percentage)
        
    def is_complete(self):
        """ Determine if the project is complete. """
        return self.completion_percentage >= 100

    def __lt__(self, other):
        return self.priority < other.priority
    
    