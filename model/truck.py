from model.parcel import Parcel
import copy


class Truck:
    """Represents a delivery truck with specific attributes and methods to manage the delivery process.

    Attributes:
        id (int): Unique identifier for the truck.
        capacity (int): Maximum number of parcels the truck can carry.
        speed (int): The speed of the truck in miles per hour.
        location (str): Current location of the truck.
        distance (int): Total distance traveled by the truck.
        parcels (list of Parcel): List of Parcel objects assigned to the truck.
        status (str): Current status of the truck (e.g., 'At the hub').
        time (int): Current time of the truck as seconds from 8:00 AM.
        total_parcels_delivered (int): Total number of parcels delivered by the truck.
    """

    def __init__(self, truck_id: int):
        """Initializes a new Truck object with the given truck_id.

        Args:
            truck_id (int): Unique identifier for the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.id = truck_id
        self.capacity = 16
        self.speed = 18
        self.location = '4001 S 700 E'
        self.distance = 0
        self.parcels = []
        self.status = 'At the hub'
        self.time = 0
        self.total_parcels_delivered = 0

    def get_truck_id(self) -> int:
        """Gets the truck ID.

        Returns:
            int: The truck ID.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.id

    def get_truck_speed(self) -> int:
        """Gets the truck speed.

        Returns:
            int: The truck speed.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.speed

    def get_truck_location(self) -> str:
        """Gets the truck location.

        Returns:
            str: The truck location.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.location

    def get_truck_parcels(self) -> list:
        """Gets the truck parcels.

        Returns:
            list: The list of Parcel objects assigned to the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.parcels

    def set_truck_location(self, new_location: str) -> None:
        """Sets the truck location.

        Args:
            new_location (str): The new location for the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.location = new_location

    def get_truck_distance(self) -> int:
        """Returns the truck distance.

        Returns:
            int: The distance traveled by the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.distance

    def add_truck_distance(self, new_distance: int):
        """Adds the specified distance to the truck's total distance.

        Args:
            new_distance (int): The distance to be added to the truck's total distance.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.distance += new_distance

    def set_truck_parcels(self, new_parcels: list):
        """Sets the truck parcels for the Truck object.

        Args:
            new_parcels (list): The list of Parcel objects to be assigned to the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.parcels = new_parcels

    def add_parcel(self, parcel: Parcel):
        """Adds a parcel to the truck.

        Args:
            parcel (Parcel): The Parcel object to be added to the truck's parcels.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.parcels.append(parcel)

    def deliver_parcel(self):
        """Removes the first parcel from the truck and updates the total parcels delivered.

        Returns:
            Parcel: The Parcel object that has been removed from the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.total_parcels_delivered += 1
        return self.parcels.pop(0)

    def get_truck_time(self) -> int:
        """Gets the truck's current time.

        Returns:
            int: The current time for the truck in seconds from 8:00 AM.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.time

    def add_truck_time(self, new_time: int) -> None:
        """Adds the specified time to the truck's current time.

        Args:
            new_time (int): The time to add to the truck's current time, in seconds.

        Note:
            The truck's time counter represents seconds from 8:00 AM.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.time += new_time

    def get_total_parcels_delivered(self) -> int:
        """Returns the total number of parcels delivered by the truck.

        Returns:
            int: The total number of parcels delivered by the truck.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.total_parcels_delivered

    def copy(self) -> 'Truck':
        """Returns a copy of the Truck object.

        The method creates a new Truck object with the same attributes as the current object.

        Returns:
            Truck: A new Truck object with the same attributes as the current object.

        Time complexity: O(n) where n is the number of parcels in the truck
        Space complexity: O(n) where n is the number of parcels in the truck
        """
        new_truck = Truck(self.id)
        new_truck.capacity = self.capacity
        new_truck.speed = self.speed
        new_truck.location = self.location
        new_truck.distance = self.distance
        new_truck.parcels = copy.copy(self.parcels)
        new_truck.status = self.status
        new_truck.time = self.time
        new_truck.total_parcels_delivered = self.total_parcels_delivered
        return new_truck
