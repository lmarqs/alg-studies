import unittest
from solution import groupAnagramWords


class Test(unittest.TestCase):

    def test_groupAnagramWords(self):
        self.assertEqual([['abc', 'cba'], ['bcd', 'cbd'], ['efg']],
                         groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))


if __name__ == '__main__':
    unittest.main()
