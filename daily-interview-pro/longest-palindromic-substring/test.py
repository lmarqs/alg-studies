import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_longestPalindrome_withEmptyString(self):
        self.assertEqual("", Solution().longestPalindrome(""))

    def test_longestPalindrome_withNoPalindrome(self):
        self.assertEqual("", Solution().longestPalindrome("abc"))

    def test_longestPalindrome_withEvenPalindrome(self):
        self.assertEqual("anana", Solution().longestPalindrome("banana"))

    def test_longestPalindrome_withPairPalindrome(self):
        self.assertEqual("racecar", Solution().longestPalindrome("tracecars"))


if __name__ == "__main__":
    unittest.main()
