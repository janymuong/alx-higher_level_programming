#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''TestCase - tests for the function max_integer:
    Function to find and return the max integer in a list of integers
    '''
    def test_max_integer(self):
        '''unit tests'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 6, 3, 5]), 6)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)
        self.assertEqual(max_integer([1, 4, 3, -4]), 4)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "four"])
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
