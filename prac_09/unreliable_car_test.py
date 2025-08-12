from unreliable_car import UnreliableCar


def main():
    # Create an unreliable car with 50% reliability
    unreliable_car = UnreliableCar("Old Clunker", 100, 50)

    # Test driving multiple times
    total_distance = 0
    successful_drives = 0
    attempts = 100

    print(f"Testing {unreliable_car.name} with {unreliable_car.reliability}% reliability")

    for i in range(attempts):
        distance_driven = unreliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1
            total_distance += distance_driven

    print(f"Attempted to drive {attempts} times")
    print(f"Successfully drove {successful_drives} times")
    print(f"Total distance driven: {total_distance}km")
    print(f"Success rate: {(successful_drives / attempts) * 100:.1f}%")
    print(f"Current odometer: {unreliable_car.odometer}km")
    print(f"Current fuel: {unreliable_car.fuel} units")


if __name__ == '__main__':
    main()