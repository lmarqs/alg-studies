import unittest
from solution import eval


class Test(unittest.TestCase):

    def test_eval(self):
        self.assertEqual(0, eval(""))
        self.assertEqual(-1, eval("-1"))
        self.assertEqual(1, eval("-1 + 2"))
        self.assertEqual(-2, eval("-1 + 2 - (3)"))
        self.assertEqual(-3, eval("-1 + 2 - (1 - 5)"))
        self.assertEqual(-3, eval("- (3 + ( 2 - 1 ) )"))


if __name__ == "__main__":
    unittest.main()
