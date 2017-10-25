#!python

from LinkedList import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        values = []

        for item in self.items():
            values.append(item[1])

        return values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items

    def length(self):  # O(N)
        """Return the length of this hash table by traversing its buckets"""
        length = 0  # Constant

        for bucket in self.buckets:  # Linear
            length += bucket.length()  # Constant

        return length  # Constant

    # We want this in Linked List but we no change it yet
    def _find_bucket(self, key):  # Constant
        """ Find a bucket using a key """

        # We get the bucket index
        bucket_index = hash(key) % len(self.buckets)  # Constant

        # Returns the bucket at an index
        return self.buckets[bucket_index]  # Constant

    def _find_node(self, key):  # O(N)
        """ Gets a node from our bucket """
        bucket = self._find_bucket(key)  # Constant

        # Set our current node
        current = bucket.head  # Constant

        # Go until our next is None
        while current is not None:  # Linear

            # If our data key is our key then we return back this node
            if current.data[0] == key:  # Constant
                return current  # Constant

            # Go to the next node
            current = current.next  # Constant

    def contains(self, key):  # O(N)
        """Return True if this hash table contains the given key, or False"""
        return self._find_node(key) is not None  # Linear

    def get(self, key):  # O(N)
        """Return the value associated with the given key, or raise KeyError"""
        node = self._find_node(key)  # Linear

        # If the Node doesn't exist raise KeyError
        if node is None:  # Constant
            raise KeyError  # Constant

        # Return the data of the node
        return node.data[1]  # Constant

    def set(self, key, value):  # O(N)
        """Insert or update the given key with its associated value"""
        node = self._find_node(key)  # Linear

        # If the Node doesn't exist we add the node
        if node is None:  # Constant
            self._find_bucket(key).append((key, value))  # Constant
            return  # Constant

        # Set the data of the node to a new value. We have to resign because Tuples are immutable.
        node.data = (key, value)  # Constant

    def delete(self, key):  # O(N) or 2n
        """ Delete a Node from the HashTable """
        node = self._find_node(key)  # O(N)

        # If we can't find the Node then raise KeyError
        if self._find_node(key) is None:  # Constant
            raise KeyError  # Constant

        # Delete the node from the bucket
        self._find_bucket(key).delete(node.data)  # O(N)
