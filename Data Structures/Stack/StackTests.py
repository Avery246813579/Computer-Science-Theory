from .Stack import Stack
import unittest


class StackTest(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        assert stack.head is None

    def test_regular(self):
        stack = Stack()
        stack.push('Dog')
        stack.push('Cat')
        assert stack.peak() == 'Cat'
        stack.pop()
        assert stack.peak() == 'Dog'
        stack.pop()
        assert stack.peak() is None

    def test_construct(self):
        stack = Stack(['Dog'])
        assert stack.pop() == 'D'
        assert stack.pop() == 'o'
        assert stack.pop() == 'D'
        assert stack.peak() is None

if __name__ == '__main__':
    unittest.main()
