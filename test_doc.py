# -*- coding: utf-8 -*-

"""Automatically-generated blanket testing for the MediaFile metadata
layer.
"""

import unittest
from phrydy import doc


class TestDoc(unittest.TestCase):

    def setUp(self):
        self.doc = doc
        self.fields = doc.fields
        self.output = doc.get_doc()

    def test_field(self):
        self.assertTrue(doc.fields)

    def test_field_title(self):
         self.assertTrue(self.fields['artist']['title'])

    def test_field_category(self):
         self.assertTrue(self.fields['artist']['category'])

    def test_field_long_title(self):
        title = self.fields['catalognum']['title']
        self.assertTrue(len(title) > 200)
        # Words at the end of a title string
        self.assertTrue('label code' in title)

    def test_doc(self):
        #print(self.output)
        self.assertTrue(isinstance(self.output, str))

    def test_get_max_key_lengths(self):
        tmp = self.fields
        tmp['looooooooooooooooooooooooooooooooooooooong'] = 'long'
        length = self.doc.get_max_key_length(tmp)
        self.assertEqual(length, 42)

if __name__ == '__main__':
    unittest.main()
