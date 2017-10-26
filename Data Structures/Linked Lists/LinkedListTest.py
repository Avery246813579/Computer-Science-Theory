#!python

from .LinkedList import LinkedList, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.next is None


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None

    def test_init_with_list(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_items(self):
        ll = LinkedList()
        assert ll.items() == []
        ll.append('A')
        assert ll.items() == ['A']
        ll.append('B')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']

    def test_length(self):
        ll = LinkedList()
        assert ll.length() == 0
        ll.append('A')
        assert ll.length() == 1
        ll.append('B')
        assert ll.length() == 2
        ll.append('C')
        assert ll.length() == 3

    def test_append(self):
        ll = LinkedList()
        ll.append('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'A'
        ll.append('B')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'B'
        ll.append('C')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend('C')
        assert ll.head.data == 'C'
        assert ll.tail.data == 'C'
        ll.prepend('B')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        ll.prepend('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_delete(self):
        ll = LinkedList()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        ll.delete('A')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        ll.delete('C')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'B'
        ll.delete('B')
        assert ll.head is None
        assert ll.tail is None
        with self.assertRaises(ValueError):
            ll.delete('D')

    def test_find(self):
        ll = LinkedList()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'D') is None

    def test_reverse_three(self):
        ll = LinkedList()
        ll.append('1')
        ll.append('2')
        ll.append('3')
        assert ll.items() == ['1', '2', '3']
        ll.reverse()
        assert ll.items() == ['3', '2', '1']

    def test_reverse_two(self):
        ll = LinkedList()
        ll.append('1')
        ll.append('2')
        assert ll.items() == ['1', '2']
        ll.reverse()
        print(ll)
        assert ll.items() == ['2', '1']

    def test_reverse_one(self):
        ll = LinkedList()
        ll.append('1')
        assert ll.items() == ['1']
        ll.reverse()
        print(ll)
        assert ll.items() == ['1']


if __name__ == '__main__':
    unittest.main()