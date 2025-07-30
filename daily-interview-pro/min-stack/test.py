import unittest
from solution import minStack


class Test(unittest.TestCase):

    def test_minStack(self):
        x = minStack()
        x.push(-2)
        x.push(0)
        x.push(-3)
        self.assertEqual(-3, x.getMin())
        self.assertEqual(-3, x.pop())
        self.assertEqual(0, x.top())
        self.assertEqual(-2, x.getMin())


if __name__ == "__main__":
    unittest.main()
