# -*- coding: utf-8 -*-

from phrydy.utils import bytestring_path
import os
import sys

# Test resources path.
RSRC = bytestring_path(os.path.join(os.path.dirname(__file__), 'files'))

# Dummy item creation.
_item_ident = 0

# OS feature test.
HAVE_SYMLINK = sys.platform != 'win32'
