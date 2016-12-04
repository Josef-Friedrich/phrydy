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

    def test_composer_sort(self):
        media = MediaFile(get_file('work.mp3'))
        self.assertEqual(media.composer_sort, u'Mozart, Wolfgang Amadeus')


class TestMusicBrainz(unittest.TestCase):

    def test_work(self):
        for extension in [
            'aiff',
            'alac.m4a',
            'flac',
            'm4a',
            'mp3',
            'mpc',
            'ogg',
            'opus',
            'wma',
            'wv'
        ]:
            media = MediaFile(get_file('mb.' + extension))
            self.assertEqual(
                media.work,
                u'Estampes, L. 100: I. Pagodes. Mod\xe9r\xe9ment anim\xe9',
                msg='work: ' + extension
            )
            self.assertEqual(
                media.composer_sort,
                u'Debussy, Claude',
                msg='composer_sort: ' + extension
            )
            self.assertEqual(
                media.mb_workid,
                u'71d55229-3dd9-3f62-b82e-d5c1444b8e04',
                msg='mb_workid: ' + extension
            )


if __name__ == '__main__':
    unittest.main()
