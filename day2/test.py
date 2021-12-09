#! /usr/env/python3

# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:
# 
# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
# 
# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

import unittest
from day2 import get_location

class TestDay2(unittest.TestCase):
    
    def test_example1(self):
        input_data = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2',
        ]
        self.assertEqual(get_location(input_data), 150)
        
    def test_example2(self):
        input_data = [
            'forward 20',
            'down 5',
            'forward -10',
            'up 3',
            'down 8',
            'forward 9',
            'down 8',
            'forward 2',
            'up 2',
        ]
        self.assertEqual(get_location(input_data), 336)


if __name__ == '__main__':
    unittest.main()
