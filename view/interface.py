import helper.time_converter as tc
import helper.data_handler as dh
import os

from model.truck import Truck


def cli(historical_truck_data, historical_parcel_data):
    """
    Provides an interface for the user to view the status and info of any package at any time, and the total mileage
    traveled by all trucks.

    Args:
        historical_truck_data (dict): A dictionary with timestamps as keys and Truck objects as values
        historical_parcel_data (dict): A dictionary with timestamps as keys and ParcelHash objects as values
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

    # CLI loop
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

        # Find total number of packages delivered
        total_parcels_delivered = 0
        for bucket in hash_table.get_table():
            if bucket is not None:
                for parcel in bucket:
                    if parcel.get_status() == 'Delivered':
                        total_parcels_delivered += 1


        # Display the CLI menu
        print("\n\nWGU Package Management System")
        print("--------------------------------")
        print("Total Number of Packages Delivered: " + str(total_parcels_delivered))
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
        print("10. Show list of late packages")
        print("11. Exit")

        # Handle user input
        choice = input("Enter a command (1-9): ")
        if choice == "1":
            new_time = input("Enter new time (24h) HH:MM  ")
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
            print("\nLate packages:")
            hash_table = set_late_status(hash_table)
            lates = []
            for slot in hash_table.get_table():
                if slot is not None:
                    for p in slot:
                        if p.get_status() == "Late":
                            lates.append(p)
            if len(lates) == 0:
                print("None")
            else:
                for p in lates:
                    print(p)
            input("Press enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "11":
            break


def set_late_status(hash_table):
    """
    Sets the status of a package to late if it is late.

    Args:
        hash_table (ParcelHash): The hash table containing the parcel data

    Returns:
        ParcelHash: The updated hash table with the late status set for the packages

    Complexity Analysis:
        Time Complexity: O(n), where n is the number of packages in the hash table.
                         We iterate through all the packages in the hash table once.
        Space Complexity: O(1), we do not use any additional data structures or memory.
    """
    # Iterate through all the slots in the hash table
    for slot in hash_table.get_table():
        # Check if the slot is not empty
        if slot is not None:
            # Iterate through all the packages in the slot
            for p in slot:
                # Check if the package has a delivery deadline of EOD (end of day)
                if p.get_delivery_deadline() == "EOD":
                    continue
                else:
                    # Convert the delivery deadline and delivery time to seconds
                    deadline = tc.timestamp_to_seconds(p.get_delivery_deadline())
                    delivery_time = p.get_delivery_time()

                    # Check if the delivery time is later than the deadline
                    if deadline < delivery_time:
                        # Set the status of the package to late
                        p.set_status("Late")

    # Return the updated hash table
    return hash_table


def find_key(truck_data, current_time):
    """
    Finds the key of the truck data that are just below the current time. Return None if no keys are found.

    Args:
        truck_data (dict): The dictionary containing the truck data with keys representing timestamps.
        current_time (float): The current time in seconds.

    Returns:
        float or None: The key (timestamp) of the truck data just below the current time, or None if no keys are found.

    Complexity Analysis:
        Time Complexity: O(n), where n is the number of items in the truck_data dictionary.
                         We filter the truck_data once and then find the maximum key.
        Space Complexity: O(n), where n is the number of items in the truck_data dictionary.
                          We create a new filtered_data dictionary which can have at most n items.
    """
    # Filter the truck_data dictionary to include only items with keys (timestamps) less than or equal to current_time
    filtered_data = {k: v for k, v in truck_data.items() if k <= current_time}

    # Check if there are no keys found in filtered_data
    if not filtered_data:
        return None

    # Find the maximum key (timestamp) in the filtered_data dictionary
    truck_key = max(filtered_data.keys())

    # Return the truck_key
    return truck_key
