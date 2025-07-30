import unittest
from solution import rearrangeString


class Test(unittest.TestCase):

    def test_rearrangeString(self):
        self.assertEquals("cbcabc", rearrangeString("abbccc"))


if __name__ == "__main__":
    unittest.main()
