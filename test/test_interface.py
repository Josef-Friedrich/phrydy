"""Test public api / interface
"""

import unittest
import phrydy
from phrydy import MediaFileExtended
import os
from test import _common


class TestInterface(unittest.TestCase):

    def test_mediafile_class_in_init(self):
        mediafile = MediaFileExtended(os.path.join(_common.RSRC,
                                             b'full.mp3'))
        self.assertEqual(mediafile.title, u'full')

    def test_module_import_mediafile(self):
        mediafile = MediaFileExtended(
            os.path.join(_common.RSRC, b'full.mp3')
        )
        self.assertEqual(mediafile.title, u'full')

    def test_module_import_doc(self):
        fields = phrydy.doc.fields
        self.assertTrue(fields)

    def test_module_import_utils(self):
        utils = phrydy.utils.as_string
        self.assertTrue(utils)
