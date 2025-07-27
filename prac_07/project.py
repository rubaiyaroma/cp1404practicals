"""
Project class for the Project Management Program.
Estimate: 45 minutes
Actual: 60 minutes +
"""

import datetime

class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # should be a datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Compare Projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is completed (100%)."""
        return self.completion_percentage == 100

    def __str__(self):
        """Return string representation for displaying projects."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    @staticmethod
    def from_line(line):
        """Create a Project from a line of the data file."""
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        return Project(name, start_date, priority, cost_estimate, completion_percentage)

    def to_line(self):
        """Convert Project to a tab-separated line for saving."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}\t{date_str}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
