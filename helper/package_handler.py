import helper.time_converter as tc
import helper.nearest_neighbor as nn


def package_loader(hash_table, truck, priority):
    """Loads packages onto the truck."""
    # Get the list of deliverable packages by check for priority first.
    if priority:
        deliverable = priority_packages(hash_table, truck)
    else:
        # Get the list of non-priority deliverable packages
        deliverable = deliverable_packages(hash_table, truck)

    # Sort deliverable packages by nearest neighbor
    deliverable = nn.nearest_neighbor_sort(deliverable)

    for parcel in deliverable:
        if len(truck.get_truck_parcels()) < truck.get_truck_capacity():
            # Update the package status
            parcel.set_status('En route')
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
