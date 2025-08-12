from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi with fanciness 2
    taxi = SilverServiceTaxi("Limo", 100, 2)

    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18 km trip: ${fare}")

    # Assert test for correctness
    assert fare == 48.78, f"Expected 48.78, but got {fare}"

if __name__ == "__main__":
    main()
