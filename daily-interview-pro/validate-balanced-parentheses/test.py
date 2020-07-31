import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_lengthOfLongestSubstring_withEmptyString(self):
        self.assertEqual(True, Solution().isValid(''))

    def test_lengthOfLongestSubstring_withValidSequence(self):
        self.assertEqual(True, Solution().isValid('((()))'))
        self.assertEqual(True, Solution().isValid('[()]{}'))

    def test_lengthOfLongestSubstring_withInvalidSequence(self):
        self.assertEqual(False, Solution().isValid('({[)]'))


if __name__ == '__main__':
    unittest.main()
