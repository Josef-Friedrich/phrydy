# -*- coding: utf-8 -*-

"""Test additional meta fields not included in beets MediaFile.
"""
from __future__ import division, absolute_import, print_function

import os
from phrydy import MediaFile
import unittest
import tempfile
import shutil


def get_file(name):
    return os.path.join(os.path.dirname(__file__), 'files', name)


def copy_to_tmp(name):
    orig = get_file(name)
    tmp = os.path.join(tempfile.mkdtemp(), os.path.basename(orig))
    shutil.copyfile(orig, tmp)
    return tmp


class TestPhrydyNewFields(unittest.TestCase):

    def test_new_fields(self):

        value = u'ef8e0ef9-491e-42df-bff9-f13981da30a7'

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
            'wv',
        ]:

            for field in [
                'mb_workhierarchy_ids',
                'mb_workid',
                'releasegroup_types',
                'work',
                'work_hierarchy',
            ]:
                tmp = copy_to_tmp('mb.' + extension)
                orig = MediaFile(tmp)
                setattr(orig, field, value)
                self.assertEqual(getattr(orig, field), value)
                orig.save()

                modified = MediaFile(tmp)
                self.assertEqual(getattr(modified, field), value,
                                 msg='field: ' + field +
                                 ', extension: ' + extension)


if __name__ == '__main__':
    unittest.main()
