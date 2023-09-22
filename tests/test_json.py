import unittest
import sys
sys.path.append('.')
from src.jsonapi import jsonapi


class TestJsonMethods(unittest.TestCase): 
    my_data = {
        "hey": complex(1, 2),
        "there": range(1, 10, 3),
        73: False,
    }
    dumpy = jsonapi.dumps(my_data)
    loady = jsonapi.loads(dumpy)
    
    print('dumps: ', dumpy)
    print('loads: ', loady)
    
    # def test_dump(my_data):
    #     my_data.assertEqual(my_data, dump)
        
    # def test_load(dump): 
