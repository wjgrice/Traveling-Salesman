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

    def update(self, key, status, time):
        """
        Update the parcel in the hash table with the same package ID as the given parcel.
        """
        slot = self.hash_function(key, self.table_size)
        for parcel in self.table[slot]:
            if parcel.get_package_id() == key:
                parcel.set_status(status)
                parcel.set_delivery_time(time)
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
