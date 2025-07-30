import unittest
from solution import lookAndSay, lookAndSayNth


class Test(unittest.TestCase):
    def test_lookAndSay(self):
        self.assertEqual("", lookAndSay(""))
        self.assertEqual("11", lookAndSay("1"))
        self.assertEqual("21", lookAndSay("11"))
        self.assertEqual("31", lookAndSay("111"))
        self.assertEqual("111213", lookAndSay("123"))
        self.assertEqual("31224311", lookAndSay("1112233331"))

    def test_lookAndSayNth(self):
        self.assertEqual("1", lookAndSayNth(1))
        self.assertEqual("11", lookAndSayNth(2))
        self.assertEqual("21", lookAndSayNth(3))
        self.assertEqual("1211", lookAndSayNth(4))
        self.assertEqual("111221", lookAndSayNth(5))


if __name__ == "__main__":
    unittest.main()
