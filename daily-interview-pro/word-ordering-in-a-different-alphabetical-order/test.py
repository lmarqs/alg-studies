import unittest
from solution import isSorted


class Test(unittest.TestCase):

    def test_isSorted(self):
        self.assertEqual(
            False, isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba")
        )
        self.assertEqual(False, isSorted(["zyx", "zy"], "zyxwvutsrqponmlkjihgfedcba"))
        self.assertEqual(True, isSorted(["zyx", "zyx"], "zyxwvutsrqponmlkjihgfedcba"))
        self.assertEqual(
            True, isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba")
        )


if __name__ == "__main__":
    unittest.main()
