import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(1, Solution().fibonacci(1))
        self.assertEqual(1, Solution().fibonacci(2))
        self.assertEqual(2, Solution().fibonacci(3))
        self.assertEqual(3, Solution().fibonacci(4))
        self.assertEqual(5, Solution().fibonacci(5))
        self.assertEqual(8, Solution().fibonacci(6))
        self.assertEqual(13, Solution().fibonacci(7))
        self.assertEqual(21, Solution().fibonacci(8))
        self.assertEqual(34, Solution().fibonacci(9))
        self.assertEqual(55, Solution().fibonacci(10))
        self.assertEqual(89, Solution().fibonacci(11))
        self.assertEqual(144, Solution().fibonacci(12))
        self.assertEqual(233, Solution().fibonacci(13))


if __name__ == '__main__':
    unittest.main()
