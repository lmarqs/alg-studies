import unittest
from solution import decodeString


class Test(unittest.TestCase):

    def test_decodeString(self):
        self.assertEqual('', decodeString(''))
        self.assertEqual('abc', decodeString('abc'))
        self.assertEqual('a', decodeString('1[a]'))
        self.assertEqual('a', decodeString('1[a]'))
        self.assertEqual('ab', decodeString('1[ab]'))
        self.assertEqual('aa', decodeString('2[a]'))
        self.assertEqual('aaa', decodeString('3[a]'))
        self.assertEqual('baaa', decodeString('b3[a]'))
        self.assertEqual('aaab', decodeString('3[a]b'))
        self.assertEqual('abbcabbc', decodeString('2[a2[b]c]'))


if __name__ == '__main__':
    unittest.main()
