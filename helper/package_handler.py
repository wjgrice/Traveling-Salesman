import helper.time_converter as tc
import helper.nearest_neighbor as nn


def package_loader(hash_table, truck):
    """Loads packages onto the truck."""

    # Get the list of priority deliverable packages
    priority_deliverable = priority_packages(hash_table, truck)
    # Get the list of non-priority deliverable packages
    deliverable = deliverable_packages(hash_table, truck)

    # sort the priority packages by nearest neighbor
    priority_deliverable = nn.two_opt_sort(priority_deliverable, truck.get_truck_location())
    # Sort deliverable packages by nearest neighbor
    deliverable = nn.two_opt_sort(deliverable, truck.get_truck_location())

    truck_priority_payload = []
    # Load the priority packages onto the truck
    for parcel in priority_deliverable:
        if len(truck_priority_payload) <= truck.get_truck_priority_slots():
            # Update the package truck ID
            parcel.set_truck_id(truck.get_truck_id())
            # Load the package onto the truck
            truck_priority_payload.append(parcel)
            group = parcel.get_group()
            if len(group) > 0 & truck.get_truck_capacity() - len(truck_priority_payload) >= len(group):
                for item in group:
                    truck_priority_payload.append(item)
            else:
                truck_priority_payload.remove(parcel)

    # Load the non-priority packages onto the truck
    priority_count = len(truck_priority_payload)
    truck_bulk_payload = []
    for parcel in deliverable:
        if (len(truck_bulk_payload) + priority_count) < truck.get_truck_capacity():
            # Update the package truck ID
            parcel.set_truck_id(truck.get_truck_id())
            # Load the package onto the truck
            truck_bulk_payload.append(parcel)

    # Sort the payloads by nearest neighbor
    truck_priority_payload = nn.two_opt_sort(truck_priority_payload, truck.get_truck_location())
    if len(truck_priority_payload) > 0:
        truck_bulk_payload = nn.two_opt_sort(truck_bulk_payload, truck_priority_payload[-1].get_address())
    else:
        truck_bulk_payload = nn.two_opt_sort(truck_bulk_payload, truck.get_truck_location())

    # Combine the priority and bulk payloads
    truck_payload = truck_priority_payload + truck_bulk_payload
    # Add the payload to the truck
    for parcel in truck_payload:
        truck.add_parcel(parcel)
        hash_table.update(parcel.get_package_id(), "En Route", truck.get_truck_time())

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


def express_loader(hash_table, truck):
    """Loads express packages onto the truck."""
    hash_table.update(15, "En Route", truck.get_truck_time())
    hash_table.update(6, "En Route", truck.get_truck_time())
    hash_table.update(30, "En Route", truck.get_truck_time())
    hash_table.update(13, "En Route", truck.get_truck_time())
    hash_table.update(31, "En Route", truck.get_truck_time())
    hash_table.update(40, "En Route", truck.get_truck_time())
    truck_payload = [hash_table.search(15), hash_table.search(6), hash_table.search(30), hash_table.search(13),
                     hash_table.search(31), hash_table.search(40)]
    truck_payload = nn.two_opt_sort(truck_payload, truck.get_truck_location())
    for parcel in truck_payload:
        truck.add_parcel(parcel)
    return hash_table, truck
