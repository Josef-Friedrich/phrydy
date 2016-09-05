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

"""Some common functionality for beets' test cases."""
from __future__ import division, absolute_import, print_function

import time
import sys
import os
import tempfile
import shutil
import six
import unittest
from contextlib import contextmanager


# Mangle the search path to include the beets sources.
sys.path.insert(0, '..')
import beets.library  # noqa: E402
from beets import importer, logging  # noqa: E402
from beets.ui import commands  # noqa: E402
from beets import util  # noqa: E402
import beets  # noqa: E402

# Make sure the development versions of the plugins are used
import beetsplug  # noqa: E402

# Test resources path.
RSRC = util.bytestring_path(os.path.join(os.path.dirname(__file__), 'rsrc'))

# Propagate to root loger so nosetest can capture it
log = logging.getLogger('beets')
log.setLevel(logging.DEBUG)

# Dummy item creation.
_item_ident = 0

# OS feature test.
HAVE_SYMLINK = sys.platform != 'win32'


def item(lib=None):
    global _item_ident
    _item_ident += 1
    i = beets.library.Item(
        title=u'the title',
        artist=u'the artist',
        albumartist=u'the album artist',
        album=u'the album',
        genre=u'the genre',
        composer=u'the composer',
        grouping=u'the grouping',
        year=1,
        month=2,
        day=3,
        track=4,
        tracktotal=5,
        disc=6,
        disctotal=7,
        lyrics=u'the lyrics',
        comments=u'the comments',
        bpm=8,
        comp=True,
        path='somepath{0}'.format(_item_ident),
        length=60.0,
        bitrate=128000,
        format='FLAC',
        mb_trackid='someID-1',
        mb_albumid='someID-2',
        mb_artistid='someID-3',
        mb_albumartistid='someID-4',
        album_id=None,
    )
    if lib:
        lib.add(i)
    return i

_album_ident = 0

class Assertions(object):
    """A mixin with additional unit test assertions."""


# A test harness for all beets tests.
# Provides temporary, isolated configuration.
class TestCase(unittest.TestCase, Assertions):
    """A unittest.TestCase subclass that saves and restores beets'
    global configuration. This allows tests to make temporary
    modifications that will then be automatically removed when the test
    completes. Also provides some additional assertion methods, a
    temporary directory, and a DummyIO.
    """
    def setUp(self):
        # A "clean" source list including only the defaults.
        beets.config.read(user=False, defaults=True)

        # Direct paths to a temporary directory. Tests can also use this
        # temporary directory.
        self.temp_dir = util.bytestring_path(tempfile.mkdtemp())

        beets.config['statefile'] = \
            util.py3_path(os.path.join(self.temp_dir, b'state.pickle'))
        beets.config['library'] = \
            util.py3_path(os.path.join(self.temp_dir, b'library.db'))
        beets.config['directory'] = \
            util.py3_path(os.path.join(self.temp_dir, b'libdir'))

        # Set $HOME, which is used by confit's `config_dir()` to create
        # directories.
        self._old_home = os.environ.get('HOME')
        os.environ['HOME'] = util.py3_path(self.temp_dir)

        # Initialize, but don't install, a DummyIO.
        self.io = DummyIO()

    def tearDown(self):
        if os.path.isdir(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        if self._old_home is None:
            del os.environ['HOME']
        else:
            os.environ['HOME'] = self._old_home
        self.io.restore()

        beets.config.clear()

class LibTestCase(TestCase):
    """A test case that includes an in-memory library object (`lib`) and
    an item added to the library (`i`).
    """
    def setUp(self):
        super(LibTestCase, self).setUp()
        self.lib = beets.library.Library(':memory:')
        self.i = item(self.lib)

    def tearDown(self):
        self.lib._connection().close()
        super(LibTestCase, self).tearDown()


# Mock I/O.


class DummyOut(object):
    encoding = 'utf8'

    def __init__(self):
        self.buf = []

    def write(self, s):
        self.buf.append(s)

    def get(self):
        if six.PY2:
            return b''.join(self.buf)
        else:
            return ''.join(self.buf)

    def clear(self):
        self.buf = []


class DummyIn(object):
    encoding = 'utf8'

    def __init__(self, out=None):
        self.buf = []
        self.out = out

    def add(self, s):
        if six.PY2:
            self.buf.append(s + b'\n')
        else:
            self.buf.append(s + '\n')

class DummyIO(object):
    """Mocks input and output streams for testing UI code."""
    def __init__(self):
        self.stdout = DummyOut()
        self.stdin = DummyIn(self.stdout)

    def restore(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
