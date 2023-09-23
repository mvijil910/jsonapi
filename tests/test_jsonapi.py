import unittest
import sys
sys.path.append('.')
from src.jsonapi import jsonapi


class TestJsonMethods(unittest.TestCase): 
    
    # print('dumps: ', dumpy)
    # print('loads: ', loady)
    
    def test_dump(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        dumpy = jsonapi.dumps(my_data)
        self.assertIn("__extended_json_type__", dumpy, "test failed: dumpy failed")
            
    def test_load(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        dumpy = jsonapi.dumps(my_data)
        loady = jsonapi.loads(dumpy)
        print('loady: ', loady)
        self.assertIn("hey", loady, "test failed: loady failed")
         
if __name__ == '__main__':
    unittest.main()

