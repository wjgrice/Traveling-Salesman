import helper.time_converter as tc


class Parcel:
    """
    Represents a parcel object with various attributes like package ID, delivery address, delivery city,
    delivery state, delivery zip code, delivery deadline, package weight, and notes.

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
        loading_time (int): Earliest time the package can be loaded onto a truck.
        delivery_time (int): The time the package is delivered.
    """

    def __init__(self, package_id: int, address: str, city: str, state: str, zip_code: str, delivery_deadline: str,
                 mass: float, notes: str):
        """Creates a new Parcel object with the given attributes.

        Args:
            package_id (int): The unique identifier for the package.
            address (str): The delivery address for the package.
            city (str): The delivery city for the package.
            state (str): The delivery state for the package.
            zip_code (str): The delivery zip code for the package.
            delivery_deadline (str): The delivery deadline for the package.
            mass (float): The weight of the package.
            notes (str): Additional notes for the package.

        Time complexity: O(1)
        Space complexity: O(1)
        """
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
        self.delivery_truck = -1

    def __str__(self) -> str:
        """Returns a string representation of the Parcel object.

        The method creates a formatted string with the package ID, address, city, state, zip code, weight,
        notes, status, loading time, delivery time, and deadline.

        Returns:
            str: A formatted string representation of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        load_time_str = ""
        if self.loading_time == -1:
            load_time_str = ' NA'
        else:
            load_time_str = str(tc.seconds_to_time(int(self.loading_time)))

        delivery_time_str = ""
        if self.delivery_time == -1:
            delivery_time_str = ' NA'
        else:
            delivery_time_str = str(tc.seconds_to_time(int(self.delivery_time)))

        return f'Package ID:{self.package_id} / Address:{self.address}, {self.city}, {self.state}, ' \
               f' {self.zip_code} / Weight:{self.mass} / Notes:{self.notes} / ' \
               f'Status:{self.status} / Loading Time:{load_time_str} / ' \
               f' Delivery Time:{delivery_time_str}  / Deadline:{self.delivery_deadline} '

    def get_package_id(self) -> int:
        """Gets the package ID for the Parcel object.

        Returns:
            int: The package ID of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.package_id

    def get_address(self) -> str:
        """Gets the delivery address for the Parcel object.

        Returns:
            str: The delivery address of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.address

    def get_city(self) -> str:
        """Gets the delivery city for the Parcel object.

        Returns:
            str: The delivery city of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.city

    def get_zip(self) -> str:
        """Gets the delivery zip code for the Parcel object.

        Returns:
            str: The delivery zip code of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.zip_code

    def get_delivery_deadline(self) -> str:
        """Gets the delivery deadline for the Parcel object.

        Returns:
            str: The delivery deadline of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.delivery_deadline

    def get_mass(self) -> float:
        """Gets the weight of the Parcel object.

        Returns:
            float: The weight of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.mass

    def get_status(self) -> str:
        """Gets the current status of the Parcel object.

        Returns:
            str: The current status of the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.status

    def set_status(self, status: str) -> None:
        """Sets the status of the Parcel object to the given status.

        Args:
            status (str): The new status for the Parcel object.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.status = status

    def set_loading_time(self, loading_time: int) -> None:
        """Sets the loading time for the Parcel object to the given loading time.

        Args:
            loading_time (int): The new loading time for the Parcel object, in seconds.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.loading_time = loading_time

    def get_delivery_time(self) -> int:
        """Returns the delivery time for the Parcel object.

        Returns:
            int: The delivery time for the Parcel object, in seconds.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.delivery_time

    def set_delivery_time(self, delivery_time: int) -> None:
        """Sets the delivery time for the Parcel object to the given delivery time.

        Args:
            delivery_time (int): The delivery time to be set for the Parcel object, in seconds.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.delivery_time = delivery_time
