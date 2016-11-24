# -*- coding: utf-8 -*-

"""Test public api / interface
"""

import unittest
import phrydy
import os
from test import _common


class TestInterface(unittest.TestCase):

    def test_interface(self):
        f = phrydy.MediaFile(os.path.join(_common.RSRC, b'full.mp3'))
        self.assertEqual(f.title, u'full')
