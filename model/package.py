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
    """

    def __init__(self, package_id: str, address: str, city: str, state: str, zip_code: str, delivery_deadline: str,
                 mass: str, notes: str):
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

    def __str__(self):
        """Returns a string representation of the Parcel object."""
        return f'{self.package_id} {self.address} {self.city} {self.state} {self.zip_code} {self.delivery_deadline} ' \
               f'{self.mass} {self.notes} {self.status}'

    def __repr__(self):
        """Returns a string representation of the Parcel object suitable for the Python interpreter."""
        return f'{self.package_id} {self.address} {self.city} {self.state} {self.zip_code} {self.delivery_deadline} ' \
               f'{self.mass} {self.notes} {self.status}'

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


class ParcelHash:
    """Hash Table Data Structure implemented using a list of lists to store parcels"""
    def __init__(self, initial_size=10, load_factor=0.75):
        """
        Initializes an empty hash table with the given initial size (which is a prime number) and load factor.
        The load factor is the maximum average number of parcels per slot before resizing the hash table.
        """
        self.table_size = initial_size
        self.load_factor = load_factor
        self.num_parcels = 0
        self.table = [[] for _ in range(self.table_size)]

    def hash_function(self, key, table_size):
        """
        Calculates the hash value of the given key using a simple hash function.
        The hash value is an integer that represents the index of the slot in the hash table.
        """
        key_str = str(key)
        hash_value = 0
        for char in key_str:
            hash_value += ord(char)
        return hash_value % table_size

    def insert(self, parcel):
        """
        Inserts the given parcel into the hash table at a slot determined by the hash value of its package ID number.
        If the slot is already occupied, the function appends the parcel to the end of the list in the slot.
        If the load factor is exceeded, the hash table is resized.
        """
        key = parcel.get_package_id()  # use package ID as key
        slot = self.hash_function(key, self.table_size)
        self.table[slot].append(parcel)
        self.num_parcels += 1
        if self.num_parcels / self.table_size > self.load_factor:
            self._resize()

    def search(self, key):
        """
        Searches for the parcel with the given key (package ID) in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.
        """
        slot = self.hash_function(key, self.table_size)
        for parcel in self.table[slot]:
            if parcel.get_package_id() == key:
                return parcel
        return None

    def size(self):
        """Returns the number of parcels in the hash table"""
        return self.num_parcels

    def is_empty(self):
        """Returns True if the hash table is empty, False otherwise"""
        return self.size() == 0

    def get_table(self):
        """Returns the list of lists representing the hash table"""
        return self.table

    def _resize(self):
        """
        Resizes the hash table to twice the current size and rehashes all the parcels into the new table.
        """
        new_table_size = self.table_size * 2
        new_table = [[] for _ in range(new_table_size)]
        for slot in self.table:
            for parcel in slot:
                key = parcel.get_package_id()
                new_slot = self.hash_function(key, new_table_size)
                new_table[new_slot].append(parcel)
        self.table = new_table
        self.table_size = new_table_size

