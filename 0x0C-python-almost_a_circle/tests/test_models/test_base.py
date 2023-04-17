#!/usr/bin/python3
'''Unit tests for Base class.'''

import unittest
import os
import json

from models.base import Base


class TestBase(unittest.TestCase):
    '''This class represents the Base module test case'''
    def setUp(self):
        '''Define test variables and initializers'''
        Base._Base__nb_objects = 0

        self.mock_list = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'

    def tearDown(self):
        '''supposedly executed after each endpoint test'''
        pass

    def test_init(self):
        '''test for constructor'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        '''test for static method - for serialization
        returns the JSON string representation of a list of dictionaries
        '''
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        s = Base.to_json_string([d])
        self.assertEqual(type(s), str)
        self.assertEqual(s, self.mock_list)
        s = Base.to_json_string(None)
        self.assertEqual(s, '[]')
        s = Base.to_json_string([])
        self.assertEqual(s, '[]')

    def test_from_json_string(self):
        '''test for static method - for deserialization
        returns the list of the JSON string representation from
        '''
        s = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        l_base = Base.from_json_string(s)
        self.assertEqual(type(l_base), list)
        self.assertEqual(len(l_base), 1)
        self.assertEqual(l_base[0]['id'], 1)
        self.assertEqual(l_base[0]['x'], 2)
        self.assertEqual(l_base[0]['y'], 3)
        self.assertEqual(l_base[0]['width'], 4)
        self.assertEqual(l_base[0]['height'], 5)
        l_base = Base.from_json_string(None)
        self.assertEqual(type(l_base), list)
        self.assertEqual(len(l_base), 0)
        l_base = Base.from_json_string('')
        self.assertEqual(type(l_base), list)
        self.assertEqual(len(l_base), 0)


if __name__ == '__main__':
    unittest.main()
