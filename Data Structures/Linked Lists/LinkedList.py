#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string rxepresentation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

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

        self.tail = new_node  # Constant

    def prepend(self, item):  # O(1)
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)   # Constant
        self.count += 1  # Constant

        # If the Linked List is empty we set the head and tail to the new node
        if self.head is None:  # Constant
            self.head = new_node  # Constant
            self.tail = self.head  # Constant
        else: # Our Linked List is not empty. Set new nodes next to the previous head and set our new node as the head
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

                self.count -= 1  # Constant
                return  # Stop checking. Don't return an error

            last = current_node  # Constant
            current_node = current_node.next  # Constant

        raise ValueError

    def find(self, quality):  # O(N)
        """Return an item from this linked list satisfying the given quality"""
        current = self.head  # Constant

        while current is not None:  # O(N)
            if quality(current.data):  # We no know
                return current.data  # Constant

            current = current.next  # Constant
