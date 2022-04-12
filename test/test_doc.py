# -*- coding: utf-8 -*-

"""Automatically-generated blanket testing for the MediaFileExtended metadata
layer.
"""

import unittest
import phrydy
from phrydy.field_docs import FieldDoc
from phrydy.mediafile_extended import MediaFileExtended
import os
from jflib import Capturing


class TestPrintDebug(unittest.TestCase):

    def test_print_debug(self):
        with Capturing() as output:
            phrydy.doc_generator.print_debug(
                os.path.join(os.path.dirname(__file__), 'files', 'full.mp3'),
                MediaFileExtended,
                MediaFileExtended.readable_fields,
                False
            )

        self.assertEqual(output[-1], 'year             : 2001')


class TestDoc(unittest.TestCase):

    def test_field(self):
        self.assertTrue(phrydy.field_docs.fields)

    def test_field_title(self):
        self.assertTrue(phrydy.field_docs.fields['artist']['description'])

    def test_field_category(self):
        self.assertTrue(phrydy.field_docs.fields['artist']['category'])

    def test_field_long_title(self):
        title = phrydy.field_docs.fields['catalognum']['description']
        self.assertTrue(len(title) > 200)
        # Words at the end of a title string
        self.assertTrue('label code' in title)

    def test_doc_string(self):
        self.assertTrue(isinstance(phrydy.format_fields_as_txt(), str))

    def test_doc_length(self):
        self.assertTrue(len(phrydy.format_fields_as_txt()) > 1000)

    def test_get_max_field_lengths(self):
        tmp = phrydy.doc_generator.fields.copy()
        field_doc: FieldDoc = {
            'description': 'Description',
            'category': 'common'
        }
        tmp['looooooooooooooooooooooooooooooooooooooong'] = field_doc
        length = phrydy.doc_generator.get_max_field_length(tmp)
        self.assertEqual(length, 42)

    def test_get_additional_docs(self):
        fields: phrydy.doc_generator.FieldDocCollection = {
            'lol': {
                'description': 'loool',
                'category': 'common',
            },
        }
        output = phrydy.doc_generator.format_fields_as_txt(
            additional_fields=fields)
        self.assertTrue('loool' in output)

    def test_field_order(self):
        output = phrydy.doc_generator.format_fields_as_txt().split('\n')
        self.assertTrue('acoustid_fingerprint' in output[0])

    def test_all_fields_are_documented(self):
        for field in MediaFileExtended.fields():
            self.assertTrue(phrydy.doc_generator.fields.get(field), field)

    def test_function_merge_fields(self):
        field1 = {
            'title': {
                'description': 'The title of a audio file.',
                'category': 'ordinary',
            },
        }
        field2 = {
            'arranger': {
                'description': 'arranger',
                'category': 'ordinary',
            },
        }
        out = phrydy.doc_generator.merge_fields(field1, field2)
        self.assertEqual(out['arranger']['description'], 'arranger')
        self.assertEqual(out['title']['description'],
                         'The title of a audio file.')


if __name__ == '__main__':
    unittest.main()
