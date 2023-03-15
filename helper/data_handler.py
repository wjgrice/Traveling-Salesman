import csv
from model.parcel import Parcel
from model.parcel_hash import ParcelHash


def create_adj_matrix_from_csv(csv_file):
    """
    Create an adjacency matrix from a CSV file of distances between nodes.

    Args:
        csv_file (str): The path to the CSV file to be processed.

    Returns:
        dict: A dictionary of dictionaries representing the adjacency matrix.

    Time complexity: O(n^2) where n is the number of nodes in the graph.
    Space complexity: O(n^2) where n is the number of nodes in the graph.
    """
    # Open the CSV file
    with open(csv_file, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)

        # Read the headers of the CSV file
        headers = reader.fieldnames[1:]

        # Create two dictionaries to hold distances and their inverses
        distances = {}
        inverted_distances = {}

        # Loop through the rows of the CSV file
        for i, row in enumerate(reader):
            # Create a dictionary for the row
            dict_row = {}
            inverted_dict_row = {}

            # Loop through the cells of the row
            for header in headers:
                # Check if the cell is empty
                if row[header] == '':
                    # If so, set the distance to infinity
                    dict_row[header] = float('inf')
                    inverted_dict_row[header] = float('inf')
                else:
                    # Otherwise, set the distance to the cell value
                    distance = float(row[header])
                    dict_row[header] = distance
                    inverted_dict_row[header] = distance

                    # Also add the inverse distance to the inverted dictionary
                    inverted_distances.setdefault(header, {})[row['']] = distance

            # Add the row dictionary to the distances and inverted_distances dictionaries
            distances.setdefault(row[''], dict_row)
            inverted_distances.setdefault(row[''], inverted_dict_row)

    # Merge the distances and inverted_distances dictionaries into one
    for key, value in distances.items():
        distances[key].update(inverted_distances[key])

    # Return the distances dictionary
    return distances


def create_parcel_hash_from_csv(file_path):
    """
    Create a hashtable of parcels from a CSV file.

    Args:
        file_path (str): Path to the input CSV file

    Returns:
        ParcelHash: A hashtable object of Parcel objects.

    Time complexity: O(n), where n is the number of parcels in the CSV file.
    Space complexity: O(n), where n is the number of parcels in the CSV file.
    """
    # Initialize an empty hash table of parcels
    parcel_hash = ParcelHash()

    # Read in the CSV file and create a Parcel object for each row
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            # Extract the parcel information from the CSV row
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            mass = float(row[6])
            notes = row[7]

            # Create a Parcel object and insert it into the hash table
            parcel = Parcel(package_id, address, city, state, zip_code, delivery_deadline, mass, notes)
            parcel_hash.insert(parcel)

    return parcel_hash
