import helper.time_converter as tc
import helper.nearest_neighbor as nn


def package_loader(hash_table, truck):
    """Loads packages onto the truck."""

    # Get the list of priority deliverable packages
    priority_deliverable = priority_packages(hash_table, truck)
    # Get the list of non-priority deliverable packages
    deliverable = deliverable_packages(hash_table, truck)

    # sort the priority packages by nearest neighbor
    priority_deliverable = nn.nearest_neighbor_sort(priority_deliverable, truck.get_truck_location())
    # Sort deliverable packages by nearest neighbor
    deliverable = nn.nearest_neighbor_sort(deliverable, truck.get_truck_location())

    # Load the priority packages onto the truck
    for parcel in priority_deliverable:
        if len(truck.get_truck_parcels()) < truck.get_truck_capacity():
            # Update the package truck ID
            parcel.set_truck_id(truck.get_truck_id())
            # Load the package onto the truck
            truck.add_parcel(parcel)
            group = parcel.get_group()
            if len(group) > 0:
                for item in group:
                    truck.add_parcel(item)

    for parcel in deliverable:
        if len(truck.get_truck_parcels()) < truck.get_truck_capacity():

            # Update the package truck ID
            parcel.set_truck_id(truck.get_truck_id())
            # Load the package onto the truck
            truck.add_parcel(parcel)
    return hash_table, truck


def deliverable_packages(hash_table, truck):
    """Returns a list of packages that are deliverable.  Compares passed in truck ID to package truck ID 0 can load on
    any truck if not 0 then they must load on the truck they are assigned to, check the status of the package,
    confirm loading time is equal or before the truck_time value assuming an 8:00 am start."""
    deliverable = []
    for bucket in hash_table.get_table():
        if bucket is not None:
            for parcel in bucket:
                if parcel.get_truck_id() == 0 or parcel.get_truck_id() == truck.get_truck_id():
                    if parcel.get_status() == 'At the hub':
                        parcel_loading_time = tc.timestamp_to_seconds(parcel.get_loading_time())
                        truck_time = truck.get_truck_time()
                        if parcel_loading_time <= truck_time:
                            deliverable.append(parcel)
    return deliverable


def priority_packages(hash_table, truck):
    """Returns a list of packages that are deliverable.  Compares passed in truck ID to package truck ID 0 can load on
    any truck if not 0 then they must load on the truck they are assigned to, check the status of the package,
    confirm loading time is equal or before the truck_time value assuming an 8:00 am start.  Also checks for priority"""
    deliverable = []
    for bucket in hash_table.get_table():
        if bucket is not None:
            for parcel in bucket:
                if parcel.get_truck_id() == 0 or parcel.get_truck_id() == truck.get_truck_id():
                    if parcel.get_status() == 'At the hub' and parcel.get_priority() == 'CRITICAL':
                        parcel_loading_time = tc.timestamp_to_seconds(parcel.get_loading_time())
                        truck_time = truck.get_truck_time()
                        if parcel_loading_time <= truck_time:
                            deliverable.append(parcel)

    for bucket in hash_table.get_table():
        if bucket is not None:
            for parcel in bucket:
                if parcel.get_truck_id() == 0 or parcel.get_truck_id() == truck.get_truck_id():
                    if parcel.get_status() == 'At the hub' and parcel.get_priority() == 'PRIORITY':
                        parcel_loading_time = tc.timestamp_to_seconds(parcel.get_loading_time())
                        truck_time = truck.get_truck_time()
                        if parcel_loading_time <= truck_time:
                            deliverable.append(parcel)
    return deliverable
