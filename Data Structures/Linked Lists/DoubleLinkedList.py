class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.last = None

    def __repr__(self):
        """Return a string rxepresentation of this node"""
        return 'Node({})'.format(repr(self.data))


class DoubleyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.count = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        return self.count

    def append(self, item):  # O(1)
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)  # Constant
        self.count += 1  # Constant

        if self.head is None:  # Constant
            self.head = new_node  # Constant
        else:
            self.tail.next = new_node  # Constant
            new_node.last = self.tail

        self.tail = new_node  # Constant

    def prepend(self, item):  # O(1)
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)   # Constant
        self.count += 1  # Constant

        # If the Linked List is empty we set the head and tail to the new node
        if self.head is None:  # Constant
            self.head = new_node  # Constant
            self.tail = self.head  # Constant
        else:  # Our Linked List is not empty. Set new nodes next to the previous head and set our new node as the head
            new_node.next = self.head  # Constant
            self.head = new_node  # Constant

    def delete(self, item):  # O(N)
        """Delete the given item from this linked list, or raise ValueError"""
        last = None
        current_node = self.head

        while current_node is not None:  # O(N)
            # The current node is the ones we are looking for
            if current_node.data == item:  # Constant
                # Our tail is our current node
                if self.tail == current_node:  # Constant
                    self.tail = last  # Constant

                if last is None:  # Constant
                    # If we are the head. We set the new head to the next value.
                    self.head = current_node.next  # Constant
                else:
                    # We aint the head so we set the last nodes head to the next node (could be null. We don't care)
                    last.next = current_node.next  # Constant

                    if current_node.next is not None:
                        current_node.next.last = last

                self.count -= 1  # Constant
                return  # Stop checking. Don't return an error

            last = current_node  # Constant
            current_node = current_node.next  # Constant

        raise ValueError

    def size(self):
        """ Gets the size of the Linked List

        AVERAGE: O(1)
        """
        return self.count

    def _at_index(self, index):
        """ Helper method used to get the node at an index

        BEST: O(1)
        WORST: O(n)
        """
        next_node = self.head

        while index > -1 or next_node is not None:
            if index == 0:
                return next_node

            next_node = next_node.next
            index -= 1

        return None

    def at_index(self, index):
        """ Gets data at an index

        BEST: O(1)
        WORST: O(n)
        """
        at_index = self._at_index(index)

        if at_index is None:
            return None

        return at_index.data

    def insert(self, index, data):
        """ Inserts data at a specific index

        BEST: O(1)
        WORST: O(n)
        """
        if index == 0:
            self.prepend(data)
            return

        at_index = self._at_index(index - 1)

        if at_index is None:
            raise IndexError

        if at_index.next is None:
            self.append(data)
            return

        new_node = Node(data)

        if at_index.next is not None:
            at_index.next.last = new_node

        new_node.next = at_index.next
        at_index.next = new_node

        new_node.last = at_index

    def find(self, quality):  # O(N)
        """Return an item from this linked list satisfying the given quality"""
        current = self.head  # Constant

        while current is not None:  # O(N)
            if quality(current.data):  # We no know
                return current.data  # Constant

            current = current.next  # Constant

    def reverse(self):
        # Next node in the list
        next_node = self.head.next

        # Previous node in our list
        previous_node = self.head

        # Our head will be the tail after this is done
        self.tail = previous_node

        # Will be new last node so we don't want it's next to have anything
        self.head.next = None

        while next_node is not None:
            # Set our current node to the current next_node
            current_node = next_node

            # Set our next node to our currents next
            next_node = current_node.next

            # Set our previous node last value to the current node
            previous_node.last = current_node

            # Set our current nodes next to the previous node
            current_node.next = previous_node

            # Set our previous node to our current
            previous_node = current_node

        # Our last_node is going to be the head now
        self.head = previous_node

        # Take away our heads last
        self.head.last = None
