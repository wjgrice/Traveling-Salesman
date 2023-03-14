from model.parcel import Parcel
import copy

class Truck:
    """Model of package delivery truck for a package delivery company."""

    def __init__(self, truck_id: int):
        """Creates a new Truck object with the given attributes."""
        self.id = truck_id
        self.capacity = 16
        self.speed = 18
        self.location = '4001 S 700 E'
        self.distance = 0
        self.parcels = []
        self.status = 'At the hub'
        self.time = 0
        self.total_parcels_delivered = 0

    def __str__(self):
        """Returns a string representation of the Truck object."""
        return f'{self.id} {self.capacity} {self.speed} {self.location} {self.distance} ' \
               f'{self.parcels} {self.status}'

    def __repr__(self):
        """Returns a string representation of the Truck object suitable for the Python interpreter."""
        return f'{self.id} {self.capacity} {self.speed} {self.location} {self.distance} ' \
               f'{self.parcels} {self.status}'

    def get_truck_id(self) -> int:
        """Returns the truck ID for the Truck object."""
        return self.id

    def get_truck_capacity(self) -> int:
        """Returns the truck capacity for the Truck object."""
        return self.capacity

    def set_truck_capacity(self, new_capacity: int):
        """Sets the truck capacity for the Truck object."""
        self.capacity = new_capacity

    def get_truck_speed(self) -> int:
        """Returns the truck speed for the Truck object."""
        return self.speed

    def get_truck_location(self) -> str:
        """Returns the truck location for the Truck object."""
        return self.location

    def get_truck_parcels(self) -> list:
        """Returns the truck parcels for the Truck object."""
        return self.parcels

    def get_truck_status(self) -> str:
        """Returns the truck status for the Truck object."""
        return self.status

    def set_truck_location(self, new_location: str):
        """Sets the truck location for the Truck object."""
        self.location = new_location

    def get_truck_distance(self) -> int:
        """Returns the truck distance for the Truck object."""
        return self.distance

    def set_truck_distance(self, new_distance: int):
        """Sets the truck distance for the Truck object."""
        self.distance = new_distance

    def add_truck_distance(self, new_distance: int):
        """Adds to the truck distance for the Truck object."""
        self.distance += new_distance

    def set_truck_parcels(self, new_parcels: list):
        """Sets the truck parcels for the Truck object."""
        self.parcels = new_parcels

    def set_truck_status(self, new_status: str):
        """Sets the truck status for the Truck object."""
        self.status = new_status

    def add_parcel(self, parcel: Parcel):
        """Adds a parcel to the truck."""
        self.parcels.append(parcel)

    def remove_parcel(self, parcel: Parcel):
        """Removes a parcel from the truck."""
        self.parcels.remove(parcel)

    def deliver_parcel(self):
        """Removes the first parcel from the truck."""
        self.total_parcels_delivered += 1
        return self.parcels.pop(0)

    def get_parcel_count(self) -> int:
        """Returns the number of parcels on the truck."""
        return len(self.parcels)

    def get_truck_time(self) -> int:
        """Returns the truck time for the Truck object."""
        return self.time

    def add_truck_time(self, new_time: int):
        """Adds to the truck time for the Truck object. Counter represents seconds from 8:00 AM."""
        self.time += new_time

    def get_total_parcels_delivered(self) -> int:
        """Returns the total number of parcels delivered by the truck."""
        return self.total_parcels_delivered

    def copy(self):
        """Returns a copy of the Truck object."""
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
