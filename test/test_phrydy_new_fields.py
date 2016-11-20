# -*- coding: utf-8 -*-

"""Test additional meta fields not included in beets MediaFile.
"""
from __future__ import division, absolute_import, print_function

import os
from phrydy import MediaFile
from phrydy.utils import bytestring_path
import unittest

def get_file(name):
    return bytestring_path(os.path.join(os.path.dirname(__file__), 'files', name))

class TestWork(unittest.TestCase):

    def test_mb_workid(self):
        media = MediaFile(get_file('work.mp3'))
        self.assertEqual(media.mb_workid, u'21fe0bf0-a040-387c-a39d-369d53c251fe')

    def test_work(self):
        media = MediaFile(get_file('work.mp3'))
        self.assertEqual(media.work, u'Concerto for French Horn no. 1 in D major, K. 386b / KV 412: I. Allegro')

if __name__ == '__main__':
    unittest.main()
