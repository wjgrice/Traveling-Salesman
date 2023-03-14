import helper.time_converter as tc
import os

from model.truck import Truck


def cli(historical_truck_data, historical_parcel_data):
    """
    Provides an interface for the user to view the status and info of any package at any time, and the total mileage
    traveled by all trucks.

    :param historical_truck_data:
    :param historical_parcel_data:
    :param hash_table:
    :param truck1:
    :param truck2:
    """

    # Set clock to last delivery time
    current_time = max(historical_truck_data.keys())

    # Split historical truck data into two trucks
    truck1_data = {k: v for k, v in historical_truck_data.items() if v.get_truck_id() == 1}
    truck2_data = {k: v for k, v in historical_truck_data.items() if v.get_truck_id() == 2}

    # Create two empty truck objects
    empty_truck1 = Truck(1)
    empty_truck2 = Truck(2)

    # Add empty truck objects to the historical data with very old time values to cover edge cases
    truck1_data[-999999] = empty_truck1
    truck2_data[-999999] = empty_truck2

    while True:
        # Find the newest key just below current time value
        latest_truck1_key = find_truck_keys(truck1_data, current_time)
        latest_truck2_key = find_truck_keys(truck2_data, current_time)

        # Get the truck objects at the latest time
        truck1 = truck1_data[latest_truck1_key]
        truck2 = truck2_data[latest_truck2_key]

        print("\n\nWGU Package Management System")
        print("--------------------------------")
        print("Total Number of Packages Delivered: " + str(
            truck1.get_total_parcels_delivered() + truck2.get_total_parcels_delivered()))
        print("Total Distance: " + str(int(truck1.get_truck_distance() + truck2.get_truck_distance())) + " miles")
        print("Current Time: " + str(tc.seconds_to_time(int(current_time))))
        print("--------------------------------\n")
        print("Please enter a command:")
        print("1. Change Current Time")
        print("2. Search for a package by ID")

        choice = input("Enter a command (1-9): ")
        if choice == "1":
            new_time = input("Enter new time (24h) HH:MM:  ")
            current_time = tc.timestamp_to_seconds(new_time)
            os.system('cls' if os.name == 'nt' else 'clear')

        if choice == "2":
            package_id = input("Enter the package ID: ")
            package = hash_table.search_id(int(package_id))
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(package)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")


def find_truck_keys(truck_data, current_time):
    """
    Finds the key of the truck data that are just below the current time. Return None if no keys are found.

    :param truck_data:
    :param current_time:
    :return:
    """
    filtered_data = {k: v for k, v in truck_data.items() if k <= current_time}
    if not filtered_data:
        return None
    truck_key = max(filtered_data.keys())
    return truck_key
