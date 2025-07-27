"""
Project Management Program
Estimate: 80/90 minutes
Actual: 120 minutes plus
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            if line.strip():
                projects.append(Project.from_line(line))
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.to_line(), file=out_file)

def display_projects(projects):
    """Display incomplete and completed projects, both sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]
    print("Incomplete projects: ")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects: ")
    for p in sorted(completed):
        print(f"  {p}")

def filter_projects_by_date(projects):
    """Ask for a date, then display projects that start after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects):
    """Prompt the user for new project details and add it to the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects):
    """Choose a project to update its percentage or priority."""
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
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
            print("Invalid menu choice.")
        print(menu)
        choice = input(">>> ").lower()

    # On quit, offer to save to the default file
    save = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if save in ("yes", "y"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")

if __name__ == "__main__":
    main()