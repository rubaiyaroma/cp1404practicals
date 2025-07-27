from Guiter import Guiter

#create test Guiter guiter1 = Guiter
guiter2 = Guiter("Another Guiter", 2013, 999.99)

# Test get_age()
print(f"{guiter1.name} get_age() - Expected 101. Got {Guiter1.get_age()}")
print(f"{guiter2.name} get_age() - Expected 10. Got {Guiter2.get_age()}")

# Test is_vintage()
print(f"{guiter1.name} is_vintage() - Expected True. Got {Guiter1.is_vintage()}")
print(f"{guiter2.name} is_vintage() - Expected False. Got {Guiter2.is_vintage()}")