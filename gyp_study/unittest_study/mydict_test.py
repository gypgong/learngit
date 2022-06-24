# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    
    def test_init(self):
        d = Dict(a=2, b='testone')
        self.assertEqual(d.a, 2)
        self.assertEqual(d.b, 'testone')
        self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
        
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            key = d.empty

    def setUp(self):
        print('setup...1')
    
    def tearDown(self):
        print('tearDoen...2')


if __name__ == '__main__':
    unittest.main()

