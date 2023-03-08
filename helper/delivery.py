from helper import data_handler as dh


def deliver_parcels(hash_table, truck):
    """Delivers the packages on the truck."""
    # Define time/mph ratio
    seconds_per_mile = 3600 / truck.get_truck_speed()
    # Create distance matrix
    distances = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')

    # Loop through the list of parcels until the list is empty
    while len(truck.get_truck_parcels()) > 0:
        # Get the first parcel in the list
        delivered_parcel = truck.deliver_parcel();
        # Get the distance it took to deliver the parcel
        distance = distances[truck.get_truck_location()][delivered_parcel.get_address()]
        # Calculate the time it took to deliver the parcel
        time_to_deliver = distance * seconds_per_mile
        # Update the truck time
        truck.add_truck_time(time_to_deliver)
        # Update the truck distance
        truck.add_truck_distance(distance)
        # Update the current location
        truck.set_truck_location(delivered_parcel.get_address())
        # Update the package status
        hash_table.update(delivered_parcel.get_package_id(), 'Delivered', truck.get_truck_time())
    # Send truck back to the hub
    distance = distances[truck.get_truck_location()]['4001 S 700 E']
    time_to_deliver = distance * seconds_per_mile
    truck.add_truck_time(time_to_deliver)
    truck.add_truck_distance(distance)
    truck.set_truck_location('4001 S 700 E')
    return hash_table, truck
