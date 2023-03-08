from model.parcel import Parcel


class Truck:
    """Model of package delivery truck for a package delivery company."""

    def __init__(self, truck_id: int):
        """Creates a new Truck object with the given attributes."""
        self.truck_id = truck_id
        self.truck_capacity = 16
        self.truck_speed = 18
        self.truck_location = '4001 S 700 E'
        self.truck_distance = 0
        self.truck_parcels = []
        self.truck_status = 'At the hub'
        self.truck_time = 0

    def __str__(self):
        """Returns a string representation of the Truck object."""
        return f'{self.truck_id} {self.truck_capacity} {self.truck_speed} {self.truck_location} {self.truck_distance} ' \
               f'{self.truck_parcels} {self.truck_status}'

    def __repr__(self):
        """Returns a string representation of the Truck object suitable for the Python interpreter."""
        return f'{self.truck_id} {self.truck_capacity} {self.truck_speed} {self.truck_location} {self.truck_distance} ' \
               f'{self.truck_parcels} {self.truck_status}'

    def get_truck_id(self) -> int:
        """Returns the truck ID for the Truck object."""
        return self.truck_id

    def get_truck_capacity(self) -> int:
        """Returns the truck capacity for the Truck object."""
        return self.truck_capacity

    def set_truck_capacity(self, new_capacity: int):
        """Sets the truck capacity for the Truck object."""
        self.truck_capacity = new_capacity

    def get_truck_speed(self) -> int:
        """Returns the truck speed for the Truck object."""
        return self.truck_speed

    def get_truck_location(self) -> str:
        """Returns the truck location for the Truck object."""
        return self.truck_location

    def get_truck_distance(self) -> int:
        """Returns the truck distance for the Truck object."""
        return self.truck_distance

    def get_truck_parcels(self) -> list:
        """Returns the truck parcels for the Truck object."""
        return self.truck_parcels

    def get_truck_status(self) -> str:
        """Returns the truck status for the Truck object."""
        return self.truck_status

    def set_truck_location(self, new_location: str):
        """Sets the truck location for the Truck object."""
        self.truck_location = new_location

    def set_truck_distance(self, new_distance: int):
        """Sets the truck distance for the Truck object."""
        self.truck_distance = new_distance

    def add_truck_distance(self, new_distance: int):
        """Adds to the truck distance for the Truck object."""
        self.truck_distance += new_distance

    def set_truck_parcels(self, new_parcels: list):
        """Sets the truck parcels for the Truck object."""
        self.truck_parcels = new_parcels

    def set_truck_status(self, new_status: str):
        """Sets the truck status for the Truck object."""
        self.truck_status = new_status

    def add_parcel(self, parcel: Parcel):
        """Adds a parcel to the truck."""
        self.truck_parcels.append(parcel)

    def remove_parcel(self, parcel: Parcel):
        """Removes a parcel from the truck."""
        self.truck_parcels.remove(parcel)

    def deliver_parcel(self):
        """Removes the first parcel from the truck."""
        return self.truck_parcels.pop(0)

    def get_parcel_count(self) -> int:
        """Returns the number of parcels on the truck."""
        return len(self.truck_parcels)

    def get_truck_time(self) -> int:
        """Returns the truck time for the Truck object."""
        return self.truck_time

    def add_truck_time(self, new_time: int):
        """Adds to the truck time for the Truck object. Counter represents seconds from 8:00 AM."""
        self.truck_time += new_time
