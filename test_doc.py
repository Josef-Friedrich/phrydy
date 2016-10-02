# -*- coding: utf-8 -*-

"""Automatically-generated blanket testing for the MediaFile metadata
layer.
"""


import phrydy
from phrydy import doc

import unittest


class TestDoc(unittest.TestCase):

    def setUp(self):
        self.doc = doc
        self.fields = doc.fields
        self.output = doc.get_doc()

    def test_fields(self):
        self.assertTrue(doc.fields)

    def test_doc(self):
        self.assertTrue(isinstance(self.output, str))

    def test_get_max_key_lengths(self):
        tmp = self.fields
        tmp['looooooooooooooooooooooooooooooooooooooong'] = 'long'
        length = self.doc.get_max_key_length(tmp)
        self.assertEqual(length, 42)

if __name__ == '__main__':
    unittest.main()
