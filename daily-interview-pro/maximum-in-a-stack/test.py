import unittest
from solution import MaxStack


class Test(unittest.TestCase):
    def test_invert(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEquals(3, s.max())
        s.pop()
        s.pop()
        self.assertEquals(2, s.max())


if __name__ == "__main__":
    unittest.main()
