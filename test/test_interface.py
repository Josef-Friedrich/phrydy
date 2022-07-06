"""Test public api / interface
"""

import os
import unittest
from test import helper

import phrydy
from phrydy import MediaFileExtended


class TestInterface(unittest.TestCase):

    def test_mediafile_class_in_init(self):
        mediafile = MediaFileExtended(os.path.join(helper.TEST_RESOURCES_PATH,
                                      'full.mp3'))
        self.assertEqual(mediafile.title, 'full')

    def test_import_phrydy_media_file(self):
        self.assertEqual(phrydy.MediaFile.__name__, 'MediaFile')

    def test_import_phrydy_media_file_extended(self):
        self.assertEqual(phrydy.MediaFileExtended.__name__,
                         'MediaFileExtended')

    def test_import_phrydy_format_fields_as_txt(self):
        self.assertEqual(phrydy.format_fields_as_txt.__name__,
                         'format_fields_as_txt')

    def test_module_import_mediafile(self):
        mediafile = MediaFileExtended(
            os.path.join(helper.TEST_RESOURCES_PATH, 'full.mp3')
        )
        self.assertEqual(mediafile.title, 'full')

    def test_module_import_doc(self):
        fields = phrydy.doc_generator.fields
        self.assertTrue(fields)
