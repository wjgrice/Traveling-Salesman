import helper.time_converter as tc
import helper.data_handler as dh
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
    truck1_data[-31536000] = empty_truck1
    truck2_data[-31536000] = empty_truck2

    # Create a fresh hash from before any deliveries take place and add it to the historical data to cover edge cases
    historical_parcel_data[-31536000] = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')

    while True:
        # Find the newest key just below current time value
        latest_truck1_key = find_key(truck1_data, current_time)
        latest_truck2_key = find_key(truck2_data, current_time)

        # Get the truck objects at the latest time
        truck1 = truck1_data[latest_truck1_key]
        truck2 = truck2_data[latest_truck2_key]

        # Find the newest key just below current time value
        latest_hash_table_key = find_key(historical_parcel_data, current_time)

        # Get the hash table at the latest time before current time
        hash_table = historical_parcel_data[latest_hash_table_key]

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
        print("3. Search for a package by Address")
        print("4. Search for a package by City")
        print("5. Search for a package by Zip Code")
        print("6. Search for a package by Deadline")
        print("7. Search for a package by Weight")
        print("8. Search for a package by Status")
        print("9. Search for all packages")
        print("10. Exit")

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
                print(package)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")

        if choice == "3":
            address = input("Enter the address: ")
            package = hash_table.search_address(address)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "4":
            city = input("Enter the city: ")
            package = hash_table.search_city(city)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "5":
            zip_code = input("Enter the zip code: ")
            package = hash_table.search_zip(zip_code)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "6":
            deadline = input("Enter the deadline: ")
            package = hash_table.search_deadline(deadline)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "7":
            weight = input("Enter the weight: ")
            package = hash_table.search_weight(weight)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "8":
            status = input("Enter the status: ")
            package = hash_table.search_delivery_status(status)
            if package is not None:
                print("\nPackage found:")
                os.system('cls' if os.name == 'nt' else 'clear')
                for p in package:
                    print(p)
                input("Press enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Package not found.")
        if choice == "9":
            print("\nPackages found:")
            for slot in hash_table.get_table():
                if slot is not None:
                    for p in slot:
                        print(p)
            input("Press enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "10":
            break



def find_key(truck_data, current_time):
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
