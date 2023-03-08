import helper.data_handler as dh


def nearest_neighbor_sort(parcel_list, start_address):
    """
    Sorts a list of parcels by nearest neighbor. Starting at the hub, the nearest neighbor is found and added to
    the list.

    :param parcel_list: A list of parcels
    :param start_address: The starting address
    :return: The sorted list of parcels
    """
    current_location = start_address
    # Create the distance hash table
    distance_to_nearest = 99999999999999999
    distances_table = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')
    # Create empty sorted list and nearest neighbor object
    nearest_neighbor = None
    sorted_parcel_list = []

    # Loop through the list of parcels until the list is empty
    while len(parcel_list) > 0:
        # Iterate through the list of parcels and find the nearest neighbor
        for parcel in parcel_list:
            distance = distances_table[current_location][parcel.get_address()]
            # If the distance is less than the current nearest neighbor, update the nearest neighbor
            if distance < distance_to_nearest:
                distance_to_nearest = distance
                nearest_neighbor = parcel
                current_location = parcel.get_address()
        # Add the nearest neighbor to the sorted list and remove it from the list of parcels
        sorted_parcel_list.append(nearest_neighbor)
        parcel_list.remove(nearest_neighbor)
        # Reset the nearest neighbor and distance
        nearest_neighbor = None
        distance_to_nearest = 99999999999999999
    # Return the nearest neighbor sorted list
    return sorted_parcel_list
