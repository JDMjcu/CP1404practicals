""" 
CP1404 prac07 
Project managenent task
Estimated time: 
                10 Minutes for Class nope => 20 minutes (actual) 
                2 hr for the programm
                Start time: 11:50
                took a break froom 12:40 -> 2:00

"""

from project import Project
import datetime
DEFAULT_FILENAME = "projects.txt"

def main():
    """ Run the pythonic project managment code program. """
    
    print("Welcome to Pythonic Project Management")
    
    # Load files from default filename
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    
    # Create menu
    menu = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    print(menu)
    choice = input(">>> ").lower()
    
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(menu)
        choice = input(">>> ").lower()
    
    
    save_query = input("Would you like to save to {DEFAULT_FILENAME}?")
    if save_query.lower() == "yes" or "y":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Create a list of projects from a file. """
    # Assuming all files have the header
    projects = []
    with open(filename, 'r') as in_file:
        next(in_file)  # Skip the header
        for line in in_file:
            parts = line.strip().split('\t') # \t = tab 
            name = parts[0]
            date = parts[1]
            priority = parts[2]
            cost = parts[3]
            completion_percentage = parts[4]
            projects.append(Project(name, date, priority, cost, completion_percentage))
            
    return projects

def save_projects(filename, projects):
    """ Save a list of projects to a file. """
    print(f"dosomething with {filename}")
    
def display_projects(projects):
    """ Display the list of projects when prompted. """
    print(f"dosomething with {projects}")

def filter_projects_by_date(projects):
    """ Filter the list of projects by date instead of priority."""
    print(f"dosomething with {projects}")
    
def add_new_project(projects):
    """ Add a project to the list of projects with user input. """
    print(f"dosomething with {projects}")
    
def update_project(projects):
    """ Update a project in the list of projects."""
    print(f"dosomething with {projects}")
    

main()
