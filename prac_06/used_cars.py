class Car:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

cars = [
    Car("Blue Lightning", 2015, 15000),
    Car("Red Rocket", 2018, 18000),
    Car("Old Reliable", 2010, 8000)
]

print("Used Cars for Sale:")
for i, car in enumerate(cars, 1):
    print(f"{i}. {car.name} ({car.year}) - ${car.price}")