import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_romanToInt(self):
        self.assertEqual(1, Solution().romanToInt('I'))
        self.assertEqual(2, Solution().romanToInt('II'))
        self.assertEqual(3, Solution().romanToInt('III'))
        self.assertEqual(4, Solution().romanToInt('IV'))
        self.assertEqual(5, Solution().romanToInt('V'))
        self.assertEqual(6, Solution().romanToInt('VI'))
        self.assertEqual(7, Solution().romanToInt('VII'))
        self.assertEqual(8, Solution().romanToInt('VIII'))
        self.assertEqual(9, Solution().romanToInt('IX'))
        self.assertEqual(10, Solution().romanToInt('X'))
        self.assertEqual(11, Solution().romanToInt('XI'))
        self.assertEqual(14, Solution().romanToInt('XIV'))
        self.assertEqual(19, Solution().romanToInt('XIX'))
        self.assertEqual(90, Solution().romanToInt('XC'))
        self.assertEqual(1904, Solution().romanToInt('MCMIV'))
        self.assertEqual(1910, Solution().romanToInt('MCMX'))


if __name__ == '__main__':
    unittest.main()
