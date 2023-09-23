import unittest
import json
import sys
sys.path.append('.')
from src.jsonapi import jsonapi

class TestJsonMethods(unittest.TestCase): 
    
    def test_ExtendedEncoder(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        encode = jsonapi.MyEncoder.encode_complex(self, complex(1, 2))
        self.assertIn("real", encode, "test failed: ecode failed")
        
    def test_ExtendedEncoder_Range(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        encode = jsonapi.MyEncoder.encode_range(self, range(1, 10, 3))
        self.assertIn("start", encode, "test failed: ecode failed")
            
    def test_ExtendedDecoder(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        encode = jsonapi.MyEncoder.encode_complex(self, complex(1, 2))
        decode = jsonapi.MyDecoder.decode_complex(self, encode)
        self.assertEqual("hey", decode, "test failed: decode failed")
        
    def test_ExtendedDecoder(self):
        my_data = {
            "hey": complex(1, 2),
            "there": range(1, 10, 3),
            73: False,
        }
        encode = jsonapi.MyEncoder.encode_range(self, range(1, 10, 3))
        decode = jsonapi.MyDecoder.decode_range(self, encode)
        self.assertEqual("hey", decode, "test failed: decode failed")
         
if __name__ == '__main__':
    unittest.main()
        
    # def test_load(dump): 
