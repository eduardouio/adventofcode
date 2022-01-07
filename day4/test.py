import unittest
from day4 import Bingo

base_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class TestDay4(unittest.TestCase):

    def setUp(self) -> None:
        self.base_data = base_data
        self.bingo_entries = [
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1
        ]
        self.bingo_tables = [[
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ], [
            [3, 15, 0, 2, 22, ],
            [9, 18, 13, 17, 5, ],
            [19, 8, 7, 25, 23, ],
            [20, 11, 10, 24, 4, ],
            [14, 21, 16, 12, 6],
        ], [
            [14, 21, 17, 24, 4, ],
            [10, 16, 15, 9, 19, ],
            [18, 8, 23, 26, 20, ],
            [22, 11, 13, 6, 5, ],
            [2, 0, 12, 3, 7, ],
        ]]

        self.bingo = Bingo(self.base_data)
        return self.bingo

    def test_base_bingo_data(self):

        self.assertListEqual(self.bingo_entries, self.bingo.entries)

        for k, item in enumerate(self.bingo_tables):
            self.assertListEqual(self.bingo_tables[k], self.bingo.tables[k])

        self.assertListEqual([[[0] * 5] * 5] * 3, self.bingo.shadow_tables)

    def test_entrie_step_1(self):
        spected_shadow = [[
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ], [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
        ]]
        self.bingo.entries = self.bingo_entries[:5]
        self.bingo.run_entries()
        self.assertListEqual(spected_shadow, self.bingo.shadow_tables)

    def test_entrie_step_2(self):
        spected_shadow = [[
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ], [
            [0, 0, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
        ], [
            [1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
        ]]

        self.bingo.entries = self.bingo_entries[:11]
        self.bingo.run_entries()
        self.assertListEqual(
            spected_shadow[0][0], self.bingo.shadow_tables[0][0])

    def test_check_bingo(self):
        shadow_false = [[
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ]]

        shadow_true_vertical = [[
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0]
        ]]

        shadow_true_horizontal = [[
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]]

        self.bingo.shadow_tables = shadow_true_vertical
        self.assertTrue(self.bingo.check_bingo())
        self.assertEqual(self.bingo.win_table, 0)

        self.bingo.shadow_tables = shadow_true_horizontal
        self.assertTrue(self.bingo.check_bingo())
        self.assertEqual(self.bingo.win_table, 0)

        self.bingo.shadow_tables = shadow_false
        self.assertFalse(self.bingo.check_bingo())
        self.assertIsNone(self.bingo.win_table)

    def test_bingo_game(self):
        res = self.bingo.run_entries()
        self.assertEqual(res, 4512)

    def test_last_bingo(self):
        res = self.bingo.get_last_board()
        self.assertEqual(res, 1924)


if __name__ == '__main__':
    unittest.main()
