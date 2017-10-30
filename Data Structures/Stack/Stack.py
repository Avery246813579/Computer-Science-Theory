class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return '[Node: ' + str(self.data) + ']'


class Stack:
    def __init__(self, iterator=None):
        if iterator is not None:
            for item in iterator:
                self.push(item)

            return

        self.head = None

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            return

        old_head = self.head

        self.head = self.head.next
        return old_head.data

    def peak(self):
        if self.head is None:
            return None

        return self.head.data

    def __str__(self):
        return '[Stack: ' + str(self.head) + ']'
