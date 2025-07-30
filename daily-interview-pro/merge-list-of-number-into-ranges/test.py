import unittest
from solution import findRanges


class Test(unittest.TestCase):

    def test_dequeue(self):
        self.assertEqual(
            ["0->2", "5->5", "7->11", "15->15"],
            findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]),
        )


if __name__ == "__main__":
    unittest.main()
