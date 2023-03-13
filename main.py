# William Grice - Student ID: 010431182
import helper.data_handler as dh
import helper.delivery as dl
from model.truck import Truck
from helper.route_optimizer import two_opt_sort
from view.interface import cli


def main():
    """Main function of the program"""
    # Create the package hash table
    package_hash_table = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')
    # Create the trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    # 1st Load Priority packages
    truck1.add_parcel(package_hash_table.search_id(15))
    truck1.add_parcel(package_hash_table.search_id(1))
    truck1.add_parcel(package_hash_table.search_id(13))
    truck1.add_parcel(package_hash_table.search_id(14))
    truck1.add_parcel(package_hash_table.search_id(16))
    truck1.add_parcel(package_hash_table.search_id(20))
    truck1.add_parcel(package_hash_table.search_id(25))
    truck1.add_parcel(package_hash_table.search_id(29))
    truck1.add_parcel(package_hash_table.search_id(30))
    truck1.add_parcel(package_hash_table.search_id(31))
    truck1.add_parcel(package_hash_table.search_id(34))
    truck1.add_parcel(package_hash_table.search_id(37))
    truck1.add_parcel(package_hash_table.search_id(40))
    # 1st Load Non-priority packages
    truck1.add_parcel(package_hash_table.search_id(19))
    truck1.add_parcel(package_hash_table.search_id(4))
    truck1.add_parcel(package_hash_table.search_id(5))

    # 2nd Load Priority packages
    truck2.add_truck_time(65 * 60)  # 9:05 AM
    truck2.add_parcel(package_hash_table.search_id(6))
    # 2nd Load Non-priority packages
    truck2.add_parcel(package_hash_table.search_id(2))
    truck2.add_parcel(package_hash_table.search_id(3))
    truck2.add_parcel(package_hash_table.search_id(18))
    truck2.add_parcel(package_hash_table.search_id(36))
    truck2.add_parcel(package_hash_table.search_id(38))
    truck2.add_parcel(package_hash_table.search_id(28))
    truck2.add_parcel(package_hash_table.search_id(32))
    truck2.add_parcel(package_hash_table.search_id(7))
    truck2.add_parcel(package_hash_table.search_id(8))
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
    dl.deliver_parcels(package_hash_table, truck1)
    dl.deliver_parcels(package_hash_table, truck2)

    # 3rd Load All non-priority packages
    truck2.add_parcel(package_hash_table.search_id(9))
    truck2.add_parcel(package_hash_table.search_id(23))
    truck2.add_parcel(package_hash_table.search_id(24))
    truck2.add_parcel(package_hash_table.search_id(26))
    truck2.add_parcel(package_hash_table.search_id(27))
    truck2.add_parcel(package_hash_table.search_id(33))
    truck2.add_parcel(package_hash_table.search_id(35))
    truck2.add_parcel(package_hash_table.search_id(39))

    # Sort the packages using two-opt sort.
    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))
    # Deliver the 3rd load of packages using truck 2
    dl.deliver_parcels(package_hash_table, truck2)

    # print("Total Distance: " + str(int(truck1.get_truck_distance() + truck2.get_truck_distance())) + " miles")
    # print("------------------------------------")
    # for bucket in package_hash_table.get_table():
    #     if bucket is not None:
    #         for parcel in bucket:
    #             if parcel.get_status() == 'Delivered':
    #                 print(str(parcel.get_package_id()) + " " + str(parcel.get_status()) + " " +
    #                       str(tc.seconds_to_time(
    #                           int(parcel.get_delivery_time()))) + " " + parcel.get_delivery_deadline())
    #

    cli(package_hash_table)


if __name__ == '__main__':
    main()
