import unittest
from solution import Queue


class Test(unittest.TestCase):

    def test_dequeue(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual([1], [q.dequeue()])

        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)

        self.assertEqual([2, 3, 4, 5, 6], [q.dequeue(), q.dequeue(), q.dequeue(), q.dequeue(), q.dequeue()])


if __name__ == '__main__':
    unittest.main()
