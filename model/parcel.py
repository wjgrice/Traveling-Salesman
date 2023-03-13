import helper.time_converter as tc

class Parcel:
    """
    Represents a parcel object with various attributes like package ID, delivery address, delivery city,
    delivery state, delivery zip code, delivery deadline, package weight and notes.

    Attributes:
        package_id (int): The unique identifier for the package.
        address (str): The delivery address for the package.
        city (str): The delivery city for the package.
        state (str): The delivery state for the package.
        zip_code (str): The delivery zip code for the package.
        delivery_deadline (str): The delivery deadline for the package.
        mass (float): The weight of the package.
        notes (str): Additional notes for the package.
        status (str): The current status of the package.
        load_seq_num (int): The sequence number for the package when it is loaded onto a truck.
        loading_time (int): Earliest time the package can be loaded onto a truck.
        delivery_time (int): The time the package is delivered.
    """

    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, delivery_deadline: str,
                 mass: float, notes: str):
        """Creates a new Parcel object with the given attributes."""
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.notes = notes
        self.status = 'At the hub'
        self.loading_time = -1
        self.delivery_time = -1

    def __str__(self):
        """Returns a string representation of the Parcel object."""
        return f'Package ID:{self.package_id} / Address:{self.address}, {self.city}, {self.state}, ' \
               f' {self.zip_code} / Weight:{self.mass} / Notes:{self.notes} / ' \
               f'Status:{self.status} / Loading Time:{tc.seconds_to_time(int(self.loading_time))} / ' \
               f' Delivery Time:{tc.seconds_to_time(int(self.delivery_time))}  / Deadline:{self.delivery_deadline} '

    def get_package_id(self) -> int:
        """Returns the package ID for the Parcel object."""
        return self.package_id

    def get_address(self) -> str:
        """Returns the delivery address for the Parcel object."""
        return self.address

    def get_city(self) -> str:
        """Returns the delivery city for the Parcel object."""
        return self.city

    def get_state(self) -> str:
        """Returns the delivery state for the Parcel object."""
        return self.state

    def get_zip(self) -> str:
        """Returns the delivery zip code for the Parcel object."""
        return self.zip_code

    def get_delivery_deadline(self) -> str:
        """Returns the delivery deadline for the Parcel object."""
        return self.delivery_deadline

    def get_mass(self) -> float:
        """Returns the weight of the Parcel object."""
        return self.mass

    def get_notes(self) -> str:
        """Returns the notes for the Parcel object."""
        return self.notes

    def get_status(self) -> str:
        """Returns the current status of the Parcel object."""
        return self.status

    def set_status(self, status: str) -> None:
        """Sets the status of the Parcel object to the given status."""
        self.status = status

    def get_loading_time(self) -> int:
        """Returns the loading time for the Parcel object."""
        return self.loading_time

    def set_loading_time(self, loading_time: int) -> None:
        """Sets the loading time for the Parcel object to the given loading time."""
        self.loading_time = loading_time

    def get_delivery_time(self) -> int:
        """Returns the delivery time for the Parcel object."""
        return self.delivery_time

    def set_delivery_time(self, delivery_time: int) -> None:
        """Sets the delivery time for the Parcel object to the given delivery time."""
        self.delivery_time = delivery_time

    def get_truck_id(self) -> int:
        """Returns the truck ID for the Parcel object."""
        return self.truck_id

    def set_truck_id(self, truck_id: int) -> None:
        """Sets the truck ID for the Parcel object to the given truck ID."""
        self.truck_id = truck_id

    def get_group(self) -> list:
        """Returns the group for the Parcel object."""
        return self.group

    def set_group(self, group: list) -> None:
        """Sets the group for the Parcel object to the given group."""
        self.group = group

    def get_priority(self) -> str:
        """Returns the priority for the Parcel object."""
        return self.priority

    def set_priority(self, priority: str) -> None:
        """Sets the priority for the Parcel object to the given priority."""
        self.priority = priority
