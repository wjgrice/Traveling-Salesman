import helper.data_handler as dh
import random


def two_opt_sort(parcel_list, start_address):
    """
    Sorts a list of parcels using the 2-opt algorithm with a nearest neighbor tour as the initial tour. Starting at the hub,
    the nearest neighbor is found and added to the list, and then the 2-opt algorithm is used to improve the tour.

    :param parcel_list: A list of parcels
    :param start_address: The starting address
    :return: The sorted list of parcels
    """
    # Create the distance hash table
    distances_table = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')

    # Run the nearest neighbor algorithm to get an initial tour
    initial_tour = nearest_neighbor_sort(parcel_list, start_address)

    # Run the 2-opt algorithm to improve the tour
    improved_tour = two_opt(initial_tour, distances_table)

    # Return the improved tour
    return improved_tour


def two_opt(tour, distances):
    """
    Implements the 2-opt algorithm to improve the tour.

    :param tour: The tour to be improved
    :param distances: A matrix of distances between the cities
    :return: The improved tour
    """
    n = len(tour)
    while True:
        improvement = 0
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]
                new_distance = tour_distance(new_tour, distances)
                if new_distance < tour_distance(tour, distances):
                    tour = new_tour
                    improvement = 1
        if improvement == 0:
            break
    return tour


def tour_distance(tour, distances):
    """
    Calculates the total distance of a tour.

    :param tour: The tour to calculate the distance of
    :param distances: A matrix of distances between the cities
    :return: The total distance of the tour
    """
    total_distance = 0
    for i in range(len(tour) - 1):
        start_address = tour[i].get_address()
        end_address = tour[i + 1].get_address()
        if start_address in distances and end_address in distances[start_address]:
            total_distance += distances[start_address][end_address]
        else:
            print(f"Missing distance between addresses {start_address} and {end_address}")
    start_address = tour[-1].get_address()
    end_address = tour[0].get_address()
    if start_address in distances and end_address in distances[start_address]:
        total_distance += distances[start_address][end_address]
    else:
        print(f"Missing distance between addresses {start_address} and {end_address}")
    return total_distance





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
