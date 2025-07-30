import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_reverseWords(self):
        self.assertEqual(
            "ehT tac ni eht tah", Solution().reverseWords("The cat in the hat")
        )


if __name__ == "__main__":
    unittest.main()
