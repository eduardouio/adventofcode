import unittest
from day3 import get_value_energy, get_vital_support, get_value_common

class test_day3(unittest.TestCase):
    
    def setUp(self) -> None:
        self.input_data = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010',
        ]
        
    def test_get_value_example1(self): 
        self.assertEqual(get_value_energy(self.input_data), 198)
    
    def test_get_value_most_common(self):
        spected_data = [
            '11110',
            '10110',
            '10111',
            '10101',
            '11100',
            '10000',
            '11001',
        ]
        self.assertListEqual(get_value_common(
            self.input_data, 0, True),
            spected_data
        )
    
    def test_get_value_not_comon(self):
        spected_data = [
            '00100',
            '01111',
            '00111',
            '00010',
            '01010',
        ]
        self.assertListEqual(get_value_common(
            self.input_data, 0, False),
            spected_data
        )
    
    def test_get_most_common_lastp(self):
        spected_data = [
            '00100',
            '11110',
            '10110',
            '11100',
            '10000',
            '00010',
            '01010',
        ]
        self.assertListEqual(
            get_value_common(self.input_data, 4, True),
            spected_data
        )
        
    def test_improbable_input_most_common(self):
        improblable_input_1 = [
            '01010',
        ] 
        
        improbable_input_2 = [
            '00000',
            '11111',
        ]
        
        improbable_input_3 = [
            '11111',
            '11111',
        ]
        
        improblable_input_4 = [
            '01111',
            '01010'
        ]
        
        self.assertListEqual(
            get_value_common(improblable_input_1, 0, True),
            ['01010']
        )
        
        self.assertListEqual(
            get_value_common(improbable_input_2, 0, True),
            ['11111']
        )
        
        self.assertListEqual(
            get_value_common(improbable_input_3, 0, True),
            ['11111', '11111']
        )
        
        self.assertEqual(
            get_value_common(improblable_input_4, 2, False),
            ['01010']
        )
        
        
    def test_get_oxigen(self):
        self.assertEqual(get_vital_support(self.input_data), 230)
    
      
if __name__ == '__main__':
    unittest.main()