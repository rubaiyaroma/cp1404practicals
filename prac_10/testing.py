"""
Testing and Assert examples - TODO: Follow instructions
"""

import doctest


def repeat_string(s, n):
    """
    Repeat a string s, n times.

    >>> repeat_string('hello', 3)
    'hellohellohello'
    >>> repeat_string('a', 5)
    'aaaaa'
    >>> repeat_string('', 4)
    ''
    """
    return s * n  # Fixed: changed + to * for proper repetition


def is_long_word(word, length=5):
    """
    Determine if a word is longer than the given length (default is 5).

    >>> is_long_word('hello')
    True
    >>> is_long_word('hi')
    False
    >>> is_long_word('wonderful', 7)
    True
    >>> is_long_word('short', 10)
    False
    """
    return len(word) > length  # Fixed: changed >= to > to match the expected behavior


def format_as_sentence(phrase):
    """
    Format a phrase as a proper sentence - starting with capital letter and ending with a single full stop.

    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('this is a test')
    'This is a test.'
    >>> format_as_sentence('already a sentence.')
    'Already a sentence.'
    >>> format_as_sentence('multiple punctuation!!')
    'Multiple punctuation.'
    >>> format_as_sentence('')
    ''
    """
    if not phrase:
        return ''

    # Capitalize first letter
    formatted = phrase[0].upper() + phrase[1:] if phrase else phrase

    # Remove any trailing punctuation and add a single full stop
    while formatted and formatted[-1] in '.!?':
        formatted = formatted[:-1]

    return formatted + '.' if formatted else '.'


class Car:
    def __init__(self, fuel=0):
        """
        Initialise a Car with a given fuel level.

        >>> car = Car()
        >>> car.fuel
        0
        >>> car = Car(10)
        >>> car.fuel
        10
        """
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance


# Assert tests for Car class
def test_car_fuel():
    """Test that Car sets fuel correctly."""
    # Test default fuel value
    car1 = Car()
    assert car1.fuel == 0, "Default fuel should be 0"

    # Test specified fuel value
    car2 = Car(15)
    assert car2.fuel == 15, "Car should set fuel to specified value"

    # Test negative fuel (edge case)
    car3 = Car(-5)
    assert car3.fuel == -5, "Car should accept negative fuel values"

    print("All Car fuel tests passed!")


# Run the tests
if __name__ == '__main__':
    # Test the repeat_string function with assert
    assert repeat_string('hello', 3) == 'hellohellohello'
    assert repeat_string('a', 5) == 'aaaaa'
    assert repeat_string('', 4) == ''
    print("All repeat_string tests passed!")

    # Test Car fuel setting
    test_car_fuel()

    # Run doctests
    doctest.testmod(verbose=True)