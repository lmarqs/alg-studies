import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_lengthOfLongestSubstring_withEmptyString(self):
        self.assertEqual(0, Solution().lengthOfLongestSubstring(""))

    def test_lengthOfLongestSubstring_withSingleChar(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("a"))

    def test_lengthOfLongestSubstring_withOnlyRepeatingChars(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("aaa"))

    def test_lengthOfLongestSubstring_withNoRepeatingChars(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abc"))

    def test_lengthOfLongestSubstring_withOneRepeatingCharsAtTheBeginingOfTheString(
        self,
    ):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("aabc"))

    def test_lengthOfLongestSubstring_withTwoRepeatingCharsAtTheBeginingOfTheString(
        self,
    ):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("aabc"))

    def test_lengthOfLongestSubstring_withOneRepeatingCharsAtTheEndOfTheString(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcc"))

    def test_lengthOfLongestSubstring_withTwoRepeatingCharsAtTheEndOfTheString(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcc"))

    def test_lengthOfLongestSubstring_withTwoRepeatingCharsAtTheMiddleOfTheString(self):
        self.assertEqual(2, Solution().lengthOfLongestSubstring("abbc"))

    def test_lengthOfLongestSubstring_withInternetSamples(self):
        self.assertEqual(3, Solution().lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(3, Solution().lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(7, Solution().lengthOfLongestSubstring("geeksforgeeks"))
        self.assertEqual(6, Solution().lengthOfLongestSubstring("abdefgabef"))

    def test_lengthOfLongestSubstring_withHardestCase(self):
        self.assertEqual(10, Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"))


if __name__ == "__main__":
    unittest.main()
