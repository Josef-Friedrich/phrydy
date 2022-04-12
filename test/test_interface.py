"""Test public api / interface
"""

import unittest
import os

from test import helper

import phrydy
from phrydy import MediaFileExtended


class TestInterface(unittest.TestCase):

    def test_mediafile_class_in_init(self):
        mediafile = MediaFileExtended(os.path.join(helper.TEST_RESOURCES_PATH,
                                      'full.mp3'))
        self.assertEqual(mediafile.title, 'full')

    def test_module_import_mediafile(self):
        mediafile = MediaFileExtended(
            os.path.join(helper.TEST_RESOURCES_PATH, 'full.mp3')
        )
        self.assertEqual(mediafile.title, 'full')

    def test_module_import_doc(self):
        fields = phrydy.doc_generator.fields
        self.assertTrue(fields)
