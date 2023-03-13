import helper.data_handler as dh
import helper.delivery as dl
import helper.time_converter as tc
from helper.package_handler import package_loader
from helper.package_handler import express_loader
from helper.sort import set_conditional_flags
from model.truck import Truck
from helper.route_optimizer import two_opt_sort
import helper.time_converter as tc


def main():
    """Main function of the program"""
    # Create the package hash table
    package_hash_table = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')
    # Set the conditional flags for the packages
    package_hash_table = set_conditional_flags(package_hash_table)
    # Create the trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    # 1st Load Priority packages
    truck1.add_parcel(package_hash_table.search(15))
    truck1.add_parcel(package_hash_table.search(1))
    truck1.add_parcel(package_hash_table.search(13))
    truck1.add_parcel(package_hash_table.search(14))
    truck1.add_parcel(package_hash_table.search(16))
    truck1.add_parcel(package_hash_table.search(20))
    truck1.add_parcel(package_hash_table.search(25))
    truck1.add_parcel(package_hash_table.search(29))
    truck1.add_parcel(package_hash_table.search(30))
    truck1.add_parcel(package_hash_table.search(31))
    truck1.add_parcel(package_hash_table.search(34))
    truck1.add_parcel(package_hash_table.search(37))
    truck1.add_parcel(package_hash_table.search(40))
    # 1st Load Non-priority packages
    truck1.add_parcel(package_hash_table.search(19))
    truck1.add_parcel(package_hash_table.search(4))
    truck1.add_parcel(package_hash_table.search(5))

    # 2nd Load Priority packages
    truck2.add_truck_time(65 * 60)  # 9:05 AM
    truck2.add_parcel(package_hash_table.search(6))
    # 2nd Load Non-priority packages
    truck2.add_parcel(package_hash_table.search(2))
    truck2.add_parcel(package_hash_table.search(3))
    truck2.add_parcel(package_hash_table.search(18))
    truck2.add_parcel(package_hash_table.search(36))
    truck2.add_parcel(package_hash_table.search(38))
    truck2.add_parcel(package_hash_table.search(28))
    truck2.add_parcel(package_hash_table.search(32))
    truck2.add_parcel(package_hash_table.search(7))
    truck2.add_parcel(package_hash_table.search(8))
    truck2.add_parcel(package_hash_table.search(10))
    truck2.add_parcel(package_hash_table.search(11))
    truck2.add_parcel(package_hash_table.search(12))
    truck2.add_parcel(package_hash_table.search(17))
    truck2.add_parcel(package_hash_table.search(21))
    truck2.add_parcel(package_hash_table.search(22))

    truck1.set_truck_parcels(two_opt_sort(truck1.get_truck_parcels(), truck1.get_truck_location()))
    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))

    dl.deliver_parcels(package_hash_table, truck1)
    dl.deliver_parcels(package_hash_table, truck2)

    # 3rd Load All non-priority packages
    truck2.add_parcel(package_hash_table.search(9))
    truck2.add_parcel(package_hash_table.search(23))
    truck2.add_parcel(package_hash_table.search(24))
    truck2.add_parcel(package_hash_table.search(26))
    truck2.add_parcel(package_hash_table.search(27))
    truck2.add_parcel(package_hash_table.search(33))
    truck2.add_parcel(package_hash_table.search(35))
    truck2.add_parcel(package_hash_table.search(39))

    truck2.set_truck_parcels(two_opt_sort(truck2.get_truck_parcels(), truck2.get_truck_location()))

    dl.deliver_parcels(package_hash_table, truck2)

    print("Total Distance: " + str(int(truck1.get_truck_distance() + truck2.get_truck_distance())) + " miles")
    print("------------------------------------")
    for bucket in package_hash_table.get_table():
        if bucket is not None:
            for parcel in bucket:
                if parcel.get_status() == 'Delivered':
                    print(str(parcel.get_package_id()) + " " + str(parcel.get_status()) + " " +
                          str(tc.seconds_to_time(
                              int(parcel.get_delivery_time()))) + " " + parcel.get_delivery_deadline())


if __name__ == '__main__':
    main()
