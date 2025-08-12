from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes fanciness and a flagfall charge."""

    flagfall = 4.50  # fixed cost for every new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness scaling."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale the base price_per_km for this instance
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 2)

    def __str__(self):
        """Return a string representation with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
