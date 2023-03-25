import copy
from helper import data_handler as dh
from helper import time_converter as tc


def deliver_parcels(hash_table, truck, historical_truck_data, historical_parcel_data):
    """
    Delivers the packages on the truck.

    Args:
        hash_table (HashTable): A hash table containing parcels to be delivered.
        truck (Truck): The truck object responsible for delivering parcels.
        historical_truck_data (dict): A dictionary containing historical truck data.
        historical_parcel_data (dict): A dictionary containing historical parcel data.

    Returns:
        tuple: Updated hash_table and truck after delivering parcels.

    Time complexity: O(n^2), where n is the number of parcels in the hash table.
    Space complexity: O(n), where n is the number of parcels in the hash table.
    """
    # Update parcel status to 'En Route' and set loading time
    for parcel in truck.get_truck_parcels():
        hash_table.search_id(parcel.get_package_id()).set_status('En Route')
        hash_table.search_id(parcel.get_package_id()).set_loading_time(truck.get_truck_time())

    # Define time/mph ratio
    seconds_per_mile = 3600 / truck.get_truck_speed()
    # Create distance matrix
    distances = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')

    # Loop through the list of parcels until the list is empty
    while len(truck.get_truck_parcels()) > 0:
        # Get the first parcel in the list
        delivered_parcel = truck.deliver_parcel()
        # Get the distance it took to deliver the parcel
        distance = distances[truck.get_truck_location()][delivered_parcel.get_address()]
        # Calculate the time of delivery
        time_to_deliver = distance * seconds_per_mile
        # Update the truck time
        truck.add_truck_time(time_to_deliver)
        # Update the truck distance
        truck.add_truck_distance(distance)
        # Update the current location
        truck.set_truck_location(delivered_parcel.get_address())
        # Update the package status
        hash_table.update(delivered_parcel.get_package_id(), 'Delivered', truck.get_truck_time())
        # Add this delivery to the historical data
        historical_truck_data[truck.get_truck_time()] = truck.copy()
        historical_parcel_data[truck.get_truck_time()] = copy.deepcopy(hash_table)

    # Send truck back to the hub if there are more deliveries
    more_deliveries = False
    for bucket in hash_table.get_table():
        for package in bucket:
            if package.get_status() == 'At Hub':
                more_deliveries = True
                break

    if more_deliveries:
        distance = distances[truck.get_truck_location()]['4001 S 700 E']
        time_to_deliver = distance * seconds_per_mile
        truck.add_truck_time(time_to_deliver)
        truck.add_truck_distance(distance)
        truck.set_truck_location('4001 S 700 E')

    return hash_table, truck, historical_truck_data, historical_parcel_data
