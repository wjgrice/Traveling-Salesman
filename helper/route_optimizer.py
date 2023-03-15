import helper.data_handler as dh


def two_opt_sort(parcel_list, start_address):
    """
    Sorts a list of parcels using the 2-opt algorithm with a nearest neighbor route as the initial route.
    Starting at the hub, the nearest neighbor is found and added to the list, and then the 2-opt algorithm is
    used to improve the route.

    Args:
        parcel_list (list): A list of parcels.
        start_address (str): The starting address.

    Returns:
        list: The sorted list of parcels.

    Time complexity: O(n^2), where n is the number of parcels.
    Space complexity: O(n), where n is the number of parcels.
    """
    # Create the distance hash table
    distances_table = dh.create_adj_matrix_from_csv('data/WGUPS Distance Table.csv')

    # Run the nearest neighbor algorithm to get an initial route
    initial_route = nearest_neighbor_sort(parcel_list, start_address)

    # Run the 2-opt algorithm to improve the route
    improved_route = two_opt(initial_route, distances_table)

    # Return the improved route
    return improved_route


def two_opt(route, distances):
    """
    Implements the 2-opt algorithm to improve the route.

    Args:
        route (list): The route to be improved.
        distances (dict): A matrix of distances between the cities.

    Returns:
        list: The improved route.

    Time complexity: O(n^2), where n is the number of cities in the route.
    Space complexity: O(n), where n is the number of cities in the route.
    """
    n = len(route)

    # Keep searching for improvements until no more improvements are found
    while True:
        improvement = 0

        # Iterate through all pairs of non-consecutive addresses in the route
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue  # Skip consecutive cities

                # Create a new route by reversing the addresses between i and j
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]

                # Calculate the distance of the new route
                new_distance = route_distance(new_route, distances)

                # If the new route has a shorter distance, update the route and record the improvement
                if new_distance < route_distance(route, distances):
                    route = new_route
                    improvement = 1

        # If no improvements were found, break the loop and return the improved route
        if improvement == 0:
            break

    return route


def route_distance(route, distances):
    """
    Calculates the total distance of a route.

    Args:
        route (list): The route to calculate the distance of.
        distances (dict): A matrix of distances between the cities.

    Returns:
        float: The total distance of the route.

    Time complexity: O(n), where n is the number of cities in the route.
    Space complexity: O(1).
    """
    total_distance = 0

    # Loop through the route and calculate the distance between consecutive cities
    for i in range(len(route) - 1):
        start_address = route[i].get_address()
        end_address = route[i + 1].get_address()

        # Check if the distances between the two cities are available in the distance matrix
        if start_address in distances and end_address in distances[start_address]:
            total_distance += distances[start_address][end_address]
        else:
            print(f"Missing distance between addresses {start_address} and {end_address}")

    # Calculate the distance between the last city in the route and the first city to complete the loop
    start_address = route[-1].get_address()
    end_address = route[0].get_address()

    # Check if the distances between the last and first cities are available in the distance matrix
    if start_address in distances and end_address in distances[start_address]:
        total_distance += distances[start_address][end_address]
    else:
        print(f"Missing distance between addresses {start_address} and {end_address}")

    return total_distance


def nearest_neighbor_sort(parcel_list, start_address):
    """
    Sorts a list of parcels by nearest neighbor. Starting at the hub, the nearest neighbor is found and added to
    the list.

    Args:
        parcel_list (list): A list of parcels.
        start_address (str): The starting address.

    Returns:
        list: The sorted list of parcels.

    Time complexity: O(n^2), where n is the number of parcels.
    Space complexity: O(n), where n is the number of parcels.
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
        # List to hold parcels with the same nearest address
        same_address_parcels = []
        # Iterate through the list of parcels and find the nearest neighbor
        for parcel in parcel_list:
            distance = distances_table[current_location][parcel.get_address()]
            # If the distance is less than the current nearest neighbor, update the nearest neighbor
            if distance < distance_to_nearest:
                distance_to_nearest = distance
                nearest_neighbor = parcel
                current_location = parcel.get_address()
        # Add the nearest neighbor to the same address parcels list
        same_address_parcels.append(nearest_neighbor)
        # Remove it from the list of parcels
        parcel_list.remove(nearest_neighbor)

        # Check for other parcels with the same address as the nearest neighbor
        for parcel in parcel_list[:]:
            if parcel.get_address() == nearest_neighbor.get_address():
                same_address_parcels.append(parcel)
                parcel_list.remove(parcel)

        # Add the parcels with the same address to the sorted list
        sorted_parcel_list.extend(same_address_parcels)

        # Reset the nearest neighbor and distance
        nearest_neighbor = None
        distance_to_nearest = 99999999999999999
    # Return the nearest neighbor sorted list
    return sorted_parcel_list
