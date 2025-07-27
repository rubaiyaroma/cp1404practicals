"""
Estimated time: 25/30 minutes
Realtime: 17/20 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing  # "Dynamic" or "Static"
        self.reflection = reflection  # True or False
        self.year = year  # Year created

    def is_dynamic(self):
        return self.typing == "Dynamic"  # Simplified the if/else

    def __str__(self):
        return f"{self.name} ({self.year}), {self.typing}, Reflection={'Yes' if self.reflection else 'No'}"