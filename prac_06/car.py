class Car:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.year}) - ${self.price}"