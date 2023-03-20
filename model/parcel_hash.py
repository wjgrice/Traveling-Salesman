import copy


class ParcelHash:
    """
    ParcelHash is a Hash Table Data Structure implemented using a list of lists to store parcels.
    It provides methods to insert, search, and update parcel information based on various criteria.
    """

    def __init__(self, initial_size=10, load_factor=0.75):
        """
        Initializes an empty hash table with the given initial size and load factor.
        The load factor is the maximum average number of parcels per slot before resizing the hash table.

        Args:
            initial_size (int): Initial size of the hash table.
            load_factor (float): Maximum average number of parcels per slot.

        Space complexity: O(n), where n is the initial size of the hash table.
        """
        self.table_size = initial_size
        self.load_factor = load_factor
        self.num_parcels = 0
        self.table = [[] for _ in range(self.table_size)]

    def __deepcopy__(self, memo):
        """
        Creates a deep copy of the ParcelHash object.

        Args:
            memo (dict): A dictionary of already copied objects.

        Returns:
            ParcelHash: A new instance of the ParcelHash class with a deep copy of the current object's data.

        Space complexity: O(n), where n is the number of parcels in the hash table.
        """
        new_obj = ParcelHash(self.table_size, self.load_factor)
        new_obj.num_parcels = self.num_parcels
        new_obj.table = copy.deepcopy(self.table, memo)
        return new_obj

    def hash_function(self, key, table_size):
        """
        Calculates the hash value of the given key using a simple hash function.
        The hash value is an integer that represents the index of the slot in the hash table.

        Args:
            key (int): The key to be hashed (package ID).
            table_size (int): The size of the hash table.

        Returns:
            int: The hash value (index of the slot in the hash table).

        Time complexity: O(k), where k is the length of the key (number of digits in the package ID).
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

        Args:
            parcel (Parcel): The parcel object to be inserted.

        Time complexity: O(1) average case, O(n) worst case, where n is the number of parcels in the hash table.
        """
        key = parcel.get_package_id()  # use package ID as key
        slot = self.hash_function(key, self.table_size)
        self.table[slot].append(parcel)
        self.num_parcels += 1
        if self.num_parcels / self.table_size > self.load_factor:
            self._resize()

    def remove(self, key):
        """
        Removes the parcel with the given key (package ID) from the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            key (int): The package ID of the parcel to be removed.

        Returns:
            Parcel: The parcel object if found, otherwise None.

        Time complexity: O(1) average case, O(n) worst case, where n is the number of parcels in the hash table.
        """
        slot = self.hash_function(key, self.table_size)
        for parcel in self.table[slot]:
            if parcel.get_package_id() == key:
                self.table[slot].remove(parcel)
                self.num_parcels -= 1
                return parcel
        return None

    def search_id(self, key):
        """
        Searches for the parcel with the given key (package ID) in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            key (int): The package ID of the parcel to be searched for.

        Returns:
            Parcel: The parcel object if found, otherwise None.

        Time complexity: O(1) average case, O(n) worst case, where n is the number of parcels in the hash table.
        """
        slot = self.hash_function(key, self.table_size)
        for parcel in self.table[slot]:
            if parcel.get_package_id() == key:
                return parcel
        return None

    def search_address(self, address):
        """
        Searches for the parcel with the given address in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            address (str): The address of the parcel to be searched for.

        Returns:
            list: A list of parcel objects with the given address, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        addresses = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_address() == address:
                        addresses.append(parcel)
        return addresses

    def search_deadline(self, deadline):
        """
        Searches for the parcel with the given deadline in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            deadline (str): The deadline of the parcel to be searched for.

        Returns:
            list: A list of parcel objects with the given deadline, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        deadlines = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_delivery_deadline() == deadline:
                        deadlines.append(parcel)
        return deadlines

    def search_city(self, city):
        """
        Searches for the parcel with the given city in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            city (str): The city of the parcel to be searched for.

        Returns:
            list: A list of parcel objects with the given city, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        cities = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_city() == city:
                        cities.append(parcel)
        return cities

    def search_zip(self, zip):
        """
        Searches for the parcel with the given zip code in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            zip (str): The zip code of the parcel to be searched for.

        Returns:
            list: A list of parcel objects with the given zip code, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        zips = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_zip() == zip:
                        zips.append(parcel)
        return zips

    def search_weight(self, weight):
        """
        Searches for the parcel with the given weight in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            weight (float): The weight of the parcel to be searched for.

        Returns:
            list: A list of parcel objects with the given weight, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        weights = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_mass() == float(weight):
                        weights.append(parcel)
        return weights

    def search_delivery_status(self, status):
        """
        Searches for the parcel with the given delivery status in the hash table.
        If the parcel is found, the function returns it. Otherwise, it returns None.

        Args:
            status (str): The delivery status to be searched for.

        Returns:
            list: A list of parcel objects with the given delivery status, otherwise an empty list.

        Time complexity: O(n) where n is the number of parcels in the hash table.
        """
        statuses = []
        for slot in self.table:
            if slot is not None:
                for parcel in slot:
                    if parcel.get_status() == status:
                        statuses.append(parcel)
        return statuses

    def update(self, key, status, time):
        """
        Update the parcel in the hash table with the same package ID as the given key.

        Args:
            key (int): The package ID of the parcel to be updated.
            status (str): The new delivery status.
            time (datetime): The new delivery time.

        Returns:
            Parcel: The updated parcel object, or None if the parcel is not found.

        Time complexity: O(1) on average, O(n) in the worst case where n is the number of parcels in the hash table.
        """
        slot = self.hash_function(key, self.table_size)
        for parcel in self.table[slot]:
            if parcel.get_package_id() == key:
                parcel.set_status(status)
                parcel.set_delivery_time(time)
                return parcel
        return None

    def get_table(self):
        """
        Returns the list of lists representing the hash table.

        Returns:
            list: The list of lists representing the hash table.

        Time complexity: O(1)
        """
        return self.table

    def _resize(self):
        """
        Resizes the hash table to twice the current size and rehashes all the parcels into the new table.

        Time complexity: O(n) where n is the number of parcels in the hash table.
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

