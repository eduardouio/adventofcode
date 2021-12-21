import unittest
from day4 import base_bingo_data

base_data = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

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
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15,
            25, 12, 22, 18, 20, 8, 19, 3, 26, 1
        ]
        self.bingo_tables = [
            [22, 13, 17, 11, 0,
             8, 2, 23, 4, 24,
             21, 9, 14, 16, 7,
             6, 10, 3, 18, 5,
             1, 12, 20, 15, 19],
            [3, 15, 0, 2, 22,
             9, 18, 13, 17, 5,
             19, 8, 7, 25, 23,
             20, 11, 10, 24, 4,
             14, 21, 16, 12, 6],
            [14, 21, 17, 24, 4,
             10, 16, 15, 9, 19,
             18, 8, 23, 26, 20,
             22, 11, 13, 6, 5,
             2, 0, 12, 3, 7,]
        ]
        return super().setUp()

    def test_base_bingo_data(self):
        entries, tables = base_bingo_data(self.base_data)
        self.assertListEqual(self.bingo_entries, entries)
        self.assertListEqual(self.bingo_tables, tables)
        
    
    def test_make_table(self):
        pass
    
    def test_vertical_line_bingo(self):
        pass
    
    def test_column_line_bingo(self):
        pass
    
    def test_bingo_game(self):
        pass



if __name__ == '__main__':
    unittest.main()