"""
Implementation of has table with linear probing
"""


class HashTable:

    def __init__(self, collision_resolution="linear_probe", capacity=10):
        self.capacity = capacity
        # Adding member variable to allow other implementations in future
        self.collision_resolution = collision_resolution
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum += ord(letter)
        return hash_sum % self.capacity

    def insert(self, key, value):
        """
        convert key to index
        basic checking to see if index is full
            if full, check for existing key and update
            else linear probe for next best location
        else it must be empty, insert
        """
        index = self.hash_function(key)
        # if keys[index] has a value
        while self.keys[index] is not None:
            # update if exists
            if self.keys[index] == key:
                self.values[index] = value
                return
            if self.collision_resolution == "linear_probe":
                index = (index + 1) % self.capacity
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        return None


if __name__ == "__main__":
    test_hash = HashTable()
    test_hash.insert("James", 15233)
    test_hash.insert("Pauli", 19953)
    test_hash.insert("Cocobob", 12243)
    test_hash.insert("Ninjamouse", 10013)
    test_hash.insert("Ninjamouse", 11311)
    print(test_hash.get("Ninjamouse"))
    print(test_hash.get("Telecat"))
