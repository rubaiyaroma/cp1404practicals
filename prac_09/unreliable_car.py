from car import Car
import random


class UnreliableCar(Car):
    """A version of Car that doesn't always drive when asked."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it passes reliability check."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0