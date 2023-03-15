# William Grice - Student ID: 010431182
import helper.data_handler as dh
import helper.delivery as dl
from model.truck import Truck
from helper.route_optimizer import two_opt_sort
from view.interface import cli


def main():
    """The main() function is the main entry point of the program. It creates a package hash table from a CSV file,
    creates two Truck objects, and loads them with packages according to their delivery priority. The function then
    sorts the packages for each truck using the two-opt algorithm and delivers them in sequence. Finally, the function
    displays the historical data for the delivered packages and trucks using a command-line interface.

    The program optimizes the delivery routes of the packages by sorting them using the two-opt algorithm, which swaps
    two edges in a route to create a new route with a shorter distance. The algorithm repeats this process
    until it reaches a local minimum.

    The program also tracks the historical data of the trucks and packages that were delivered, which can be displayed
    using the command-line interface.

    The program expects a CSV file with package data to be located in the data directory, and it uses helper functions
    and classes from other modules in the helper and model packages.

    Time complexity: O(n^2), where n number of packages. The programs complexity is derived from the two-opt algorithm,
    which has a time complexity of O(n^2).

    Space complexity: O(n), where n is the number of packages. The program's complexity is derived number of packages
    stored in the data structures.

    """

    # Create the package hash table
    package_hash_table = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')
    # Create the trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    # Create dictionary to hold historical truck data
    historical_truck_data = {}
    historical_parcel_data = {}

    # 1st Load Priority packages
    truck1.add_parcel(package_hash_table.search_id(15))
    truck1.add_parcel(package_hash_table.search_id(7))
    truck1.add_parcel(package_hash_table.search_id(23))
    truck1.add_parcel(package_hash_table.search_id(14))
    truck1.add_parcel(package_hash_table.search_id(16))
    truck1.add_parcel(package_hash_table.search_id(20))
    truck2.add_parcel(package_hash_table.search_id(38))
    truck1.add_parcel(package_hash_table.search_id(29))
    truck1.add_parcel(package_hash_table.search_id(4))
    truck1.add_parcel(package_hash_table.search_id(31))
    truck1.add_parcel(package_hash_table.search_id(34))
    truck1.add_parcel(package_hash_table.search_id(37))
    truck1.add_parcel(package_hash_table.search_id(40))
    # 1st Load Non-priority packages
    truck1.add_parcel(package_hash_table.search_id(19))
    truck1.add_parcel(package_hash_table.search_id(13))
    truck1.add_parcel(package_hash_table.search_id(5))

    # 2nd Load Priority packages
    truck2.add_truck_time(65 * 60)  # 9:05 AM
    truck2.add_parcel(package_hash_table.search_id(6))
    truck2.add_parcel(package_hash_table.search_id(25))
    truck2.add_parcel(package_hash_table.search_id(30))
    truck2.add_parcel(package_hash_table.search_id(1))

    # Delivery 2nd load priority packages
    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))
    dl.deliver_parcels(package_hash_table, truck2, historical_truck_data, historical_parcel_data)

    # 2nd Load Non-priority packages
    truck2.add_parcel(package_hash_table.search_id(24))
    truck2.add_parcel(package_hash_table.search_id(18))
    truck2.add_parcel(package_hash_table.search_id(36))
    truck2.add_parcel(package_hash_table.search_id(28))
    truck2.add_parcel(package_hash_table.search_id(32))
    truck2.add_parcel(package_hash_table.search_id(26))
    truck2.add_parcel(package_hash_table.search_id(10))
    truck2.add_parcel(package_hash_table.search_id(11))
    truck2.add_parcel(package_hash_table.search_id(12))
    truck2.add_parcel(package_hash_table.search_id(17))
    truck2.add_parcel(package_hash_table.search_id(21))
    truck2.add_parcel(package_hash_table.search_id(22))

    # Sort the packages using two-opt sort for each truck
    truck1.set_truck_parcels(two_opt_sort(truck1.get_truck_parcels(), truck1.get_truck_location()))
    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))

    # Deliver the 1st and 2nd load of packages
    dl.deliver_parcels(package_hash_table, truck1, historical_truck_data, historical_parcel_data)
    dl.deliver_parcels(package_hash_table, truck2, historical_truck_data, historical_parcel_data)

    # 3rd Load All non-priority packages
    truck2.add_parcel(package_hash_table.search_id(9))
    truck2.add_parcel(package_hash_table.search_id(3))
    truck2.add_parcel(package_hash_table.search_id(2))
    truck2.add_parcel(package_hash_table.search_id(8))
    truck2.add_parcel(package_hash_table.search_id(27))
    truck2.add_parcel(package_hash_table.search_id(33))
    truck2.add_parcel(package_hash_table.search_id(35))
    truck2.add_parcel(package_hash_table.search_id(39))

    # Sort the packages using two-opt sort.
    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))
    # Deliver the 3rd load of packages using truck 2
    dl.deliver_parcels(package_hash_table, truck2, historical_truck_data, historical_parcel_data)

    cli(historical_truck_data, historical_parcel_data)


if __name__ == '__main__':
    main()
