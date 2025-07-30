import unittest
from solution import word_search


class Test(unittest.TestCase):

    def test_word_search(self):
        self.assertEqual(False, word_search([], "FOAM"))
        self.assertEqual(False, word_search([[]], "FOAM"))
        self.assertEqual(False, word_search([["#"]], "FOAM"))
        self.assertEqual(True, word_search([["F", "O", "A", "M"]], "FOAM"))
        self.assertEqual(True, word_search([["#", "F", "O", "A", "M"]], "FOAM"))
        self.assertEqual(True, word_search([["F", "O", "A", "M", "#"]], "FOAM"))
        self.assertEqual(True, word_search([["#", "F", "O", "A", "M", "#"]], "FOAM"))
        self.assertEqual(True, word_search([["F"], ["O"], ["A"], ["M"]], "FOAM"))
        self.assertEqual(True, word_search([["#"], ["F"], ["O"], ["A"], ["M"]], "FOAM"))
        self.assertEqual(True, word_search([["F"], ["O"], ["A"], ["M"], ["#"]], "FOAM"))
        self.assertEqual(
            True, word_search([["#"], ["F"], ["O"], ["A"], ["M"], ["#"]], "FOAM")
        )
        self.assertEqual(
            True,
            word_search(
                [
                    ["F", "#", "#"],
                    ["O", "#", "#"],
                    ["A", "#", "#"],
                    ["M", "#", "#"],
                ],
                "FOAM",
            ),
        )
        self.assertEqual(
            True,
            word_search(
                [
                    ["#", "F", "#"],
                    ["#", "O", "#"],
                    ["#", "A", "#"],
                    ["#", "M", "#"],
                ],
                "FOAM",
            ),
        )
        self.assertEqual(
            True,
            word_search(
                [
                    ["#", "#", "F"],
                    ["#", "#", "O"],
                    ["#", "#", "A"],
                    ["#", "#", "M"],
                ],
                "FOAM",
            ),
        )


if __name__ == "__main__":
    unittest.main()
