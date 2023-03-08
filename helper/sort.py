import re


def set_conditional_flags(package_hash_table):
    """
    Sets the conditional flags for the packages by calling set_grouping, set_truck, and set_load_time.

    Time complexity: O(n), where n is the number of parcels in the hash table.

    :param package_hash_table: The hash table of parcels
    :return: The updated hash table of parcels with conditional flags set
    """
    # Set the grouping for the parcels
    set_grouping(package_hash_table)

    # Set the truck id for the parcels
    set_truck(package_hash_table)

    # Set the load time for the parcels
    set_load_time(package_hash_table)

    # Set the priority for the parcels
    set_priority(package_hash_table)

    return package_hash_table


def set_grouping(package_hash_table):
    """
    Sets the grouping for the packages. Search the notes for the words 'Must be delivered with' when it finds an
    entry with the criteria it takes the parcel ids from the notes string and adds the corresponding parcels to the
    parcel's grouping list. If the parcel doesn't have a grouping, set its grouping to an empty list.

    Time complexity: O(n^2), where n is the number of parcels in the hash table.

    :param package_hash_table: The hash table of parcels
    :return: The updated hash table of parcels with grouping set
    """
    for bucket in package_hash_table.get_table():
        for parcel in bucket:
            notes = parcel.get_notes()
            if 'Must be delivered with' in notes:
                # Extract the parcel ids from the notes string
                parcel_ids = [int(s) for s in re.findall(r'\d+', notes)]

                # Find the parcels with the corresponding ids and add them to the grouping list
                grouping = [package_hash_table.search(parcel_id) for parcel_id in parcel_ids]

                # Add the grouping to the parcel
                parcel.set_group(grouping)
            else:
                # If the parcel doesn't have a grouping, set its grouping to an empty list
                parcel.set_group([])
    return package_hash_table



def set_truck(package_hash_table):
    """
    Sets the truck for the packages. Search the notes for the words 'Can only be on truck ' when it finds an entry
    with the criteria it takes the integers from the notes string  it uses the value to set the parcel's truck value.
    If the parcel doesn't have a truck, set its truck to 0.

    Time complexity: O(n), where n is the number of parcels in the hash table.

    :param package_hash_table: The hash table of parcels
    :return: The updated hash table of parcels with truck ids set
    """
    for bucket in package_hash_table.get_table():
        for parcel in bucket:
            notes = parcel.get_notes()
            if 'Can only be on truck' in notes:
                # Extract the integers from the notes string
                truck = int(re.findall(r'\d+', notes)[0])

                # Add the truck to the parcel
                parcel.set_truck_id(truck)
            else:
                # If the parcel doesn't have a truck, set its truck to 0
                parcel.set_truck_id(0)
    return package_hash_table


def set_load_time(package_hash_table):
    """
    Sets the load time for the packages. Searches the notes for the words 'Delayed on flight' and sets the parcel's load
    time value to the time listed in the notes. If the words 'Wrong address listed' are in the notes, sets the load time
    to 10:20 am. If the parcel doesn't have either of these conditions, sets its load time to 8:00 am.

    Time complexity: O(n), where n is the number of parcels in the hash table.

    :param package_hash_table: The hash table of parcels.
    :return: The updated hash table of parcels.
    """
    # Loop through each parcel in the hash table
    for bucket in package_hash_table.get_table():
        for parcel in bucket:
            notes = parcel.get_notes()
            if 'Delayed on flight' in notes:
                # Extract the time from the notes string
                time = re.findall(r'\d+:\d+', notes)[0]

                # Set the parcel's loading time
                parcel.set_loading_time(time)
            elif 'Wrong address listed' in notes:
                # Set the parcel's loading time to 10:20 am
                parcel.set_loading_time('10:20')
            else:
                # Set the parcel's loading time to 8:00 am
                parcel.set_loading_time('8:00')

    return package_hash_table


def set_priority(package_hash_table):
    """
    Sets the priority for the packages. Searches the notes for the words 'Delayed on flight' and sets the parcel's
    priority value to 1. If the words 'Wrong address listed' are in the notes, sets the priority to 2. If the parcel
    doesn't have either of these conditions, sets its priority to 3.

    Time complexity: O(n), where n is the number of parcels in the hash table.

    :param package_hash_table: The hash table of parcels.
    :return: The updated hash table of parcels.
    """
    # Loop through each parcel in the hash table
    for bucket in package_hash_table.get_table():
        for parcel in bucket:
            deadline = parcel.get_delivery_deadline()
            if '9:00 AM' in deadline:
                parcel.set_priority("CRITICAL")
            elif '10:30 AM' in deadline:
                parcel.set_priority("PRIORITY")
            else:
                parcel.set_priority("LOW")

    return package_hash_table
