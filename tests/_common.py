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

import sys
import os
import tempfile
import shutil
import six
import unittest


# Mangle the search path to include the beets sources.
sys.path.insert(0, '..')
import beets.library  # noqa: E402
from beets import logging  # noqa: E402
from beets import util  # noqa: E402
import beets  # noqa: E402


# Test resources path.
RSRC = util.bytestring_path(os.path.join(os.path.dirname(__file__), 'rsrc'))

# Propagate to root loger so nosetest can capture it
log = logging.getLogger('beets')
log.setLevel(logging.DEBUG)

# Dummy item creation.
_item_ident = 0

# OS feature test.
HAVE_SYMLINK = sys.platform != 'win32'

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
