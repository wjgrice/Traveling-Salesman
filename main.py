import helper.data_handler as dh
import helper.delivery as dl
import helper.time_converter as tc
from helper.package_handler import package_loader
from helper.sort import set_conditional_flags
from model.truck import Truck


def main():
    """Main function of the program"""
    # Create the package hash table
    package_hash_table = dh.create_parcel_hash_from_csv('data/WGUPS Package File.csv')
    # Set the conditional flags for the packages
    package_hash_table = set_conditional_flags(package_hash_table)
    # Create the trucks
    truck1 = Truck(1)
    truck2 = Truck(2)

    # Load the packages onto the trucks by passing in the hashtable and the truck object.  The function will return
    # the updated hash table and the truck object with the packages loaded.
    truck1.set_truck_capacity(16)
    truck2.set_truck_capacity(16)
    truck2.add_truck_time(4000)

    package_hash_table, truck1 = package_loader(package_hash_table, truck1)
    package_hash_table, truck2 = package_loader(package_hash_table, truck2)

    total_packages_delivered = truck1.get_parcel_count() + truck2.get_parcel_count()
    print("First Truck Load 1: " + str(truck1.get_parcel_count()))
    print("Second Truck Load 1: " + str(truck2.get_parcel_count()))

    # Deliver packages
    package_hash_table, truck1 = dl.deliver_parcels(package_hash_table, truck1)
    package_hash_table, truck2 = dl.deliver_parcels(package_hash_table, truck2)

    # Load more packages onto the trucks
    truck1.set_truck_capacity(16)
    truck2.set_truck_capacity(16)
    package_hash_table, truck1 = package_loader(package_hash_table, truck1)
    package_hash_table, truck2 = package_loader(package_hash_table, truck2)

    print("First Truck Load 2: " + str(truck1.get_parcel_count()))
    print("Second Truck Load 2: " + str(truck2.get_parcel_count()))
    total_packages_delivered += truck1.get_parcel_count() + truck2.get_parcel_count()
    print("Total Packages Delivered: " + str(total_packages_delivered))
    print("--------------------")

    # Deliver packages
    package_hash_table, truck1 = dl.deliver_parcels(package_hash_table, truck1)
    package_hash_table, truck2 = dl.deliver_parcels(package_hash_table, truck2)

    print("First Truck Distance: " + str(int(truck1.get_truck_distance())))
    print("Second Truck Distance: " + str(int(truck2.get_truck_distance())))

    total_distance = truck1.get_truck_distance() + truck2.get_truck_distance()
    print("Total Distance " + str(total_distance))
    print("--------------------")

    for bucket in package_hash_table.get_table():
        if bucket is not None:
            for parcel in bucket:
                print(str(str(parcel.get_package_id()) + ' - ' + str(tc.seconds_to_time(int(parcel.get_delivery_time()))) + ' '
                      + str(parcel.get_delivery_deadline())) + ' - ' + str(parcel.get_group()) + ' ~ '
                      + str(parcel.get_truck_id()))


if __name__ == '__main__':
    main()
