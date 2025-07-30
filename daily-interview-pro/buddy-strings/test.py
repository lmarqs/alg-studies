import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_buddyStrings(self):
        self.assertEqual(True, Solution().buddyStrings("ab", "ba"))
        self.assertEqual(False, Solution().buddyStrings("ab", "ab"))
        self.assertEqual(True, Solution().buddyStrings("aa", "aa"))
        self.assertEqual(True, Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))
        self.assertEqual(False, Solution().buddyStrings("aaaaaabbc", "aaaaaaacb"))
        self.assertEqual(False, Solution().buddyStrings("", "aa"))


if __name__ == "__main__":
    unittest.main()
