# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
"""Specific, edge-case tests for the MediaFile metadata layer.
"""
from __future__ import division, absolute_import, print_function

import os
import shutil
import sys
import six
from tempfile import mkdtemp

import phrydy
from phrydy.utils import bytestring_path

import unittest

# Mangle the search path to include the beets sources.
sys.path.insert(0, '..')

# Test resources path.
RSRC = bytestring_path(os.path.join(os.path.dirname(__file__), 'files'))

# Dummy item creation.
_item_ident = 0

# OS feature test.
HAVE_SYMLINK = sys.platform != 'win32'

########################################################################
# helper.py
########################################################################


class TestHelper(object):
    """Helper mixin for high-level cli and plugin tests.

    This mixin provides methods to isolate beets' global state provide
    fixtures.
    """

    def create_temp_dir(self):
        """Create a temporary directory and assign it into
        `self.temp_dir`. Call `remove_temp_dir` later to delete it.
        """
        temp_dir = mkdtemp()
        self.temp_dir = bytestring_path(temp_dir)

    def remove_temp_dir(self):
        """Delete the temporary directory created by `create_temp_dir`.
        """
        shutil.rmtree(self.temp_dir)


_sc = phrydy._safe_cast


class EdgeTest(unittest.TestCase):
    def test_emptylist(self):
        # Some files have an ID3 frame that has a list with no elements.
        # This is very hard to produce, so this is just the first 8192
        # bytes of a file found "in the wild".
        emptylist = phrydy.MediaFile(os.path.join(RSRC, b'emptylist.mp3'))
        genre = emptylist.genre
        self.assertEqual(genre, None)

    def test_release_time_with_space(self):
        # Ensures that release times delimited by spaces are ignored.
        # Amie Street produces such files.
        space_time = phrydy.MediaFile(os.path.join(RSRC, b'space_time.mp3'))
        self.assertEqual(space_time.year, 2009)
        self.assertEqual(space_time.month, 9)
        self.assertEqual(space_time.day, 4)

    def test_release_time_with_t(self):
        # Ensures that release times delimited by Ts are ignored.
        # The iTunes Store produces such files.
        t_time = phrydy.MediaFile(os.path.join(RSRC, b't_time.m4a'))
        self.assertEqual(t_time.year, 1987)
        self.assertEqual(t_time.month, 3)
        self.assertEqual(t_time.day, 31)

    def test_tempo_with_bpm(self):
        # Some files have a string like "128 BPM" in the tempo field
        # rather than just a number.
        f = phrydy.MediaFile(os.path.join(RSRC, b'bpm.mp3'))
        self.assertEqual(f.bpm, 128)

    def test_discc_alternate_field(self):
        # Different taggers use different vorbis comments to reflect
        # the disc and disc count fields: ensure that the alternative
        # style works.
        f = phrydy.MediaFile(os.path.join(RSRC, b'discc.ogg'))
        self.assertEqual(f.disc, 4)
        self.assertEqual(f.disctotal, 5)

    def test_old_ape_version_bitrate(self):
        media_file = os.path.join(RSRC, b'oldape.ape')
        f = phrydy.MediaFile(media_file)
        self.assertEqual(f.bitrate, 0)

    def test_only_magic_bytes_jpeg(self):
        # Some jpeg files can only be recognized by their magic bytes and as
        # such aren't recognized by imghdr. Ensure that this still works thanks
        # to our own follow up mimetype detection based on
        # https://github.com/file/file/blob/master/magic/Magdir/jpeg#L12
        magic_bytes_file = os.path.join(RSRC, b'only-magic-bytes.jpg')
        with open(magic_bytes_file, 'rb') as f:
            jpg_data = f.read()
        self.assertEqual(phrydy._image_mime_type(jpg_data), 'image/jpeg')

    def test_soundcheck_non_ascii(self):
        # Make sure we don't crash when the iTunes SoundCheck field contains
        # non-ASCII binary data.
        f = phrydy.MediaFile(os.path.join(RSRC, b'soundcheck-nonascii.m4a'))
        self.assertEqual(f.rg_track_gain, 0.0)


class InvalidValueToleranceTest(unittest.TestCase):
    def test_safe_cast_string_to_int(self):
        self.assertEqual(_sc(int, u'something'), 0)

    def test_safe_cast_int_string_to_int(self):
        self.assertEqual(_sc(int, u'20'), 20)

    def test_safe_cast_string_to_bool(self):
        self.assertEqual(_sc(bool, u'whatever'), False)

    def test_safe_cast_intstring_to_bool(self):
        self.assertEqual(_sc(bool, u'5'), True)

    def test_safe_cast_string_to_float(self):
        self.assertAlmostEqual(_sc(float, u'1.234'), 1.234)

    def test_safe_cast_int_to_float(self):
        self.assertAlmostEqual(_sc(float, 2), 2.0)

    def test_safe_cast_string_with_cruft_to_float(self):
        self.assertAlmostEqual(_sc(float, u'1.234stuff'), 1.234)

    def test_safe_cast_negative_string_to_float(self):
        self.assertAlmostEqual(_sc(float, u'-1.234'), -1.234)

    def test_safe_cast_special_chars_to_unicode(self):
        us = _sc(six.text_type, 'caf\xc3\xa9')
        self.assertTrue(isinstance(us, six.text_type))
        self.assertTrue(us.startswith(u'caf'))

    def test_safe_cast_float_with_no_numbers(self):
        v = _sc(float, u'+')
        self.assertEqual(v, 0.0)

    def test_safe_cast_float_with_dot_only(self):
        v = _sc(float, u'.')
        self.assertEqual(v, 0.0)

    def test_safe_cast_float_with_multiple_dots(self):
        v = _sc(float, u'1.0.0')
        self.assertEqual(v, 1.0)


class SafetyTest(unittest.TestCase, TestHelper):
    def setUp(self):
        self.create_temp_dir()

    def tearDown(self):
        self.remove_temp_dir()

    def _exccheck(self, fn, exc, data=''):
        fn = os.path.join(self.temp_dir, fn)
        with open(fn, 'w') as f:
            f.write(data)
        try:
            self.assertRaises(exc, phrydy.MediaFile, fn)
        finally:
            os.unlink(fn)  # delete the temporary file

    def test_corrupt_mp3_raises_unreadablefileerror(self):
        # Make sure we catch Mutagen reading errors appropriately.
        self._exccheck(b'corrupt.mp3', phrydy.UnreadableFileError)

    def test_corrupt_mp4_raises_unreadablefileerror(self):
        self._exccheck(b'corrupt.m4a', phrydy.UnreadableFileError)

    def test_corrupt_flac_raises_unreadablefileerror(self):
        self._exccheck(b'corrupt.flac', phrydy.UnreadableFileError)

    def test_corrupt_ogg_raises_unreadablefileerror(self):
        self._exccheck(b'corrupt.ogg', phrydy.UnreadableFileError)

    def test_invalid_ogg_header_raises_unreadablefileerror(self):
        self._exccheck(b'corrupt.ogg', phrydy.UnreadableFileError,
                       'OggS\x01vorbis')

    def test_corrupt_monkeys_raises_unreadablefileerror(self):
        self._exccheck(b'corrupt.ape', phrydy.UnreadableFileError)

    def test_invalid_extension_raises_filetypeerror(self):
        self._exccheck(b'something.unknown', phrydy.FileTypeError)

    def test_magic_xml_raises_unreadablefileerror(self):
        self._exccheck(b'nothing.xml', phrydy.UnreadableFileError, "ftyp")

    @unittest.skipUnless(HAVE_SYMLINK, u'platform lacks symlink')
    def test_broken_symlink(self):
        fn = os.path.join(RSRC, b'brokenlink')
        os.symlink('does_not_exist', fn)
        try:
            self.assertRaises(phrydy.UnreadableFileError, phrydy.MediaFile, fn)
        finally:
            os.unlink(fn)


class SideEffectsTest(unittest.TestCase):
    def setUp(self):
        self.empty = os.path.join(RSRC, b'empty.mp3')

    def test_opening_tagless_file_leaves_untouched(self):
        old_mtime = os.stat(self.empty).st_mtime
        phrydy.MediaFile(self.empty)
        new_mtime = os.stat(self.empty).st_mtime
        self.assertEqual(old_mtime, new_mtime)


class MP4EncodingTest(unittest.TestCase, TestHelper):
    def setUp(self):
        self.create_temp_dir()
        src = os.path.join(RSRC, b'full.m4a')
        self.path = os.path.join(self.temp_dir, b'test.m4a')
        shutil.copy(src, self.path)

        self.mf = phrydy.MediaFile(self.path)

    def tearDown(self):
        self.remove_temp_dir()

    def test_unicode_label_in_m4a(self):
        self.mf.label = u'foo\xe8bar'
        self.mf.save()
        new_mf = phrydy.MediaFile(self.path)
        self.assertEqual(new_mf.label, u'foo\xe8bar')


class MP3EncodingTest(unittest.TestCase, TestHelper):
    def setUp(self):
        self.create_temp_dir()
        src = os.path.join(RSRC, b'full.mp3')
        self.path = os.path.join(self.temp_dir, b'test.mp3')
        shutil.copy(src, self.path)

        self.mf = phrydy.MediaFile(self.path)

    def test_comment_with_latin1_encoding(self):
        # Set up the test file with a Latin1-encoded COMM frame. The encoding
        # indices defined by MP3 are listed here:
        # http://id3.org/id3v2.4.0-structure
        self.mf.mgfile['COMM::eng'].encoding = 0

        # Try to store non-Latin1 text.
        self.mf.comments = u'\u2028'
        self.mf.save()


class ZeroLengthMediaFile(phrydy.MediaFile):
    @property
    def length(self):
        return 0.0


class MissingAudioDataTest(unittest.TestCase):
    def setUp(self):
        super(MissingAudioDataTest, self).setUp()
        path = os.path.join(RSRC, b'full.mp3')
        self.mf = ZeroLengthMediaFile(path)

    def test_bitrate_with_zero_length(self):
        del self.mf.mgfile.info.bitrate  # Not available directly.
        self.assertEqual(self.mf.bitrate, 0)


class TypeTest(unittest.TestCase):
    def setUp(self):
        super(TypeTest, self).setUp()
        path = os.path.join(RSRC, b'full.mp3')
        self.mf = phrydy.MediaFile(path)

    def test_year_integer_in_string(self):
        self.mf.year = u'2009'
        self.assertEqual(self.mf.year, 2009)

    def test_set_replaygain_gain_to_none(self):
        self.mf.rg_track_gain = None
        self.assertEqual(self.mf.rg_track_gain, 0.0)

    def test_set_replaygain_peak_to_none(self):
        self.mf.rg_track_peak = None
        self.assertEqual(self.mf.rg_track_peak, 0.0)

    def test_set_year_to_none(self):
        self.mf.year = None
        self.assertIsNone(self.mf.year)

    def test_set_track_to_none(self):
        self.mf.track = None
        self.assertEqual(self.mf.track, 0)

    def test_set_date_to_none(self):
        self.mf.date = None
        self.assertIsNone(self.mf.date)
        self.assertIsNone(self.mf.year)
        self.assertIsNone(self.mf.month)
        self.assertIsNone(self.mf.day)


class SoundCheckTest(unittest.TestCase):
    def test_round_trip(self):
        data = phrydy._sc_encode(1.0, 1.0)
        gain, peak = phrydy._sc_decode(data)
        self.assertEqual(gain, 1.0)
        self.assertEqual(peak, 1.0)

    def test_decode_zero(self):
        data = b' 80000000 80000000 00000000 00000000 00000000 00000000 ' \
               b'00000000 00000000 00000000 00000000'
        gain, peak = phrydy._sc_decode(data)
        self.assertEqual(gain, 0.0)
        self.assertEqual(peak, 0.0)

    def test_malformatted(self):
        gain, peak = phrydy._sc_decode(b'foo')
        self.assertEqual(gain, 0.0)
        self.assertEqual(peak, 0.0)

    def test_special_characters(self):
        gain, peak = phrydy._sc_decode(u'caf\xe9'.encode('utf8'))
        self.assertEqual(gain, 0.0)
        self.assertEqual(peak, 0.0)

    def test_decode_handles_unicode(self):
        # Most of the time, we expect to decode the raw bytes. But some formats
        # might give us text strings, which we need to handle.
        gain, peak = phrydy._sc_decode(u'caf\xe9')
        self.assertEqual(gain, 0.0)
        self.assertEqual(peak, 0.0)


class ID3v23Test(unittest.TestCase, TestHelper):
    def _make_test(self, ext='mp3', id3v23=False):
        self.create_temp_dir()
        src = os.path.join(RSRC, bytestring_path('full.{0}'.format(ext)))
        self.path = os.path.join(self.temp_dir,
                                 bytestring_path('test.{0}'.format(ext)))
        shutil.copy(src, self.path)
        return phrydy.MediaFile(self.path, id3v23=id3v23)

    def _delete_test(self):
        self.remove_temp_dir()

    def test_v24_year_tag(self):
        mf = self._make_test(id3v23=False)
        try:
            mf.year = 2013
            mf.save()
            frame = mf.mgfile['TDRC']
            self.assertTrue('2013' in six.text_type(frame))
            self.assertTrue('TYER' not in mf.mgfile)
        finally:
            self._delete_test()

    def test_v23_year_tag(self):
        mf = self._make_test(id3v23=True)
        try:
            mf.year = 2013
            mf.save()
            frame = mf.mgfile['TYER']
            self.assertTrue('2013' in six.text_type(frame))
            self.assertTrue('TDRC' not in mf.mgfile)
        finally:
            self._delete_test()

    def test_v23_on_non_mp3_is_noop(self):
        mf = self._make_test('m4a', id3v23=True)
        try:
            mf.year = 2013
            mf.save()
        finally:
            self._delete_test()

    def test_v24_image_encoding(self):
        mf = self._make_test(id3v23=False)
        try:
            mf.images = [phrydy.Image(b'test data')]
            mf.save()
            frame = mf.mgfile.tags.getall('APIC')[0]
            self.assertEqual(frame.encoding, 3)
        finally:
            self._delete_test()

    @unittest.skip("a bug, see #899")
    def test_v23_image_encoding(self):
        """For compatibility with OS X/iTunes (and strict adherence to
        the standard), ID3v2.3 tags need to use an inferior text
        encoding: UTF-8 is not supported.
        """
        mf = self._make_test(id3v23=True)
        try:
            mf.images = [phrydy.Image(b'test data')]
            mf.save()
            frame = mf.mgfile.tags.getall('APIC')[0]
            self.assertEqual(frame.encoding, 1)
        finally:
            self._delete_test()


if __name__ == '__main__':
    unittest.main()