def cli(hash_table):
    """
    Provides an interface for the user to view the status and info of any package at any time, and the total mileage
    traveled by all trucks.

    :param total_mileage: The total mileage traveled by all trucks
    """
    while True:
        print("\n\nWGUPS Package Management System")
        print("--------------------------------")
        print("Please enter a command:")
        print("1. Search for a package by ID")
        print("2. Search for packages by address")
        print("3. Search for packages by delivery deadline")
        print("4. Search for packages by city")
        print("5. Search for packages by zip code")
        print("6. Search for packages by weight")
        print("7. Search for packages by delivery status")
        print("8. View total mileage traveled by all trucks")
        print("9. Exit")

        choice = input("Enter a command (1-9): ")
        if choice == "1":
            package_id = input("Enter the package ID: ")
            package = hash_table.search_id(int(package_id))
            if package is not None:
                print(package)
            else:
                print("Package not found.")
        elif choice == "2":
            address = input("Enter the address: ")
            packages = hash_table.search_address(address)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found at this address.")
        elif choice == "3":
            deadline = input("Enter the delivery deadline (in format 'HH:MM:SS AM/PM'): ")
            packages = hash_table.search_deadline(deadline)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found with this deadline.")
        elif choice == "4":
            city = input("Enter the city: ")
            packages = hash_table.search_city(city)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found in this city.")
        elif choice == "5":
            zip = input("Enter the zip code: ")
            packages = hash_table.search_zip(zip)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found with this zip code.")
        elif choice == "6":
            weight = input("Enter the weight: ")
            packages = hash_table.search_weight(weight)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found with this weight.")
        elif choice == "7":
            status = input("Enter the delivery status: ")
            packages = self.search_delivery_status(status)
            if packages is not None:
                for package in packages:
                    print(package)
            else:
                print("No packages found with this delivery status.")
        elif choice == "8":
            print(f"\nTotal mileage traveled by all trucks: {5001} miles")
        elif choice == "9":
            print("\nExiting WGUPS Package Management System...")
            break
        else:
            print("\nInvalid command. Please enter a number from 1-9.")
