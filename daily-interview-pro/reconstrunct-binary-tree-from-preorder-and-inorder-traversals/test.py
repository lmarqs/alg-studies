import unittest
from solution import reconstruct


class Test(unittest.TestCase):
    def test_reconstruct(self):
        self.assertEqual(
            "abcdefg",
            reconstruct(
                ["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"]
            ).__str__(),
        )


if __name__ == "__main__":
    unittest.main()
