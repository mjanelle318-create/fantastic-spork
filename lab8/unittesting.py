"""
janelle moncrieffe 
sep 30, 2026
lab 8: unittest
"""

import unittest
from calculations import *

def addnumbers(a, b):
    return a + b

# create a unit test for addnumbers

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addnumbers(2, 3), 5) 
        # Test if 2+3 is eqal to 5
        self.assertEqual(addnumbers(), 0) 
        self.assertEqual(addnumbers(5),5) 

    def test_subtraction(self):
        self.assertEqual(subtractingnumbers(5,6),-1)
        self.assertEqual(subtractingnumbers(3),3)
        self.assertEqual(subtractingnumbers(7,3),4)
        self.assertEqual(subtractingnumbers(),0)
    
    def test_multiplication(self):
        self.assertEqual(multiplyingnumbers(3,2),6)
        self.assertEqual(multiplyingnumbers(5),5)
        self.assertEqual(multiplyingnumbers(),1)

    def test_division(self):
        self.assertEqual(dividenumbers(7,2),3.5)
        self.assertAlmostEqual(dividenumbers(7,3),2.33, places=3)

    def test_dividebyzero(self):
        self.assertIsNone(dividenumbers(10,0))

    def test_valueerror(self):
        self.assertIsNone(dividenumbers(10,'a'))
        self.assertIsNone(dividenumbers('a','b'))
        
    def test_unexpected_exception(self):
        # test other possible errors by mocking
        with self.assertRaises(Exception):
            # passing None to trigger an ex
            dividenumbers()

if __name__ == "__main__":
    unittest.main()