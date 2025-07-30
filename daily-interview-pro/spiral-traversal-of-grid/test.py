import unittest
from solution import matrix_spiral_print


class Test(unittest.TestCase):

    def test_matrix_spiral_print(self):
        grid = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]

        self.assertEquals(
            "1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12",
            matrix_spiral_print(grid),
        )


if __name__ == "__main__":
    unittest.main()
