# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Thomas Scholtes.
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

"""This module includes various helpers that provide fixtures, capture
information or mock the environment.

- The `control_stdin` and `capture_stdout` context managers allow one to
  interact with the user interface.

- `has_program` checks the presence of a command on the system.

- The `generate_album_info` and `generate_track_info` functions return
  fixtures to be used when mocking the autotagger.

- The `TestImportSession` allows one to run importer code while
  controlling the interactions through code.

- The `TestHelper` class encapsulates various fixtures that can be set up.
"""


from __future__ import division, absolute_import, print_function

import shutil
from tempfile import mkdtemp

import beets
import beets.plugins
from beets.library import Item, Album
from beets import importer
from beets import util

class TestHelper(object):
    """Helper mixin for high-level cli and plugin tests.

    This mixin provides methods to isolate beets' global state provide
    fixtures.
    """
    # TODO automate teardown through hook registration

    def load_plugins(self, *plugins):
        """Load and initialize plugins by names.

        Similar setting a list of plugins in the configuration. Make
        sure you call ``unload_plugins()`` afterwards.
        """
        # FIXME this should eventually be handled by a plugin manager
        beets.config['plugins'] = plugins
        beets.plugins.load_plugins(plugins)
        beets.plugins.find_plugins()
        # Take a backup of the original _types to restore when unloading
        Item._types.update(beets.plugins.types(Item))
        Album._types.update(beets.plugins.types(Album))

    # Library fixtures methods

    def create_item(self, **values):
        """Return an `Item` instance with sensible default values.

        The item receives its attributes from `**values` paratmeter. The
        `title`, `artist`, `album`, `track`, `format` and `path`
        attributes have defaults if they are not given as parameters.
        The `title` attribute is formated with a running item count to
        prevent duplicates. The default for the `path` attribute
        respects the `format` value.

        The item is attached to the database from `self.lib`.
        """
        item_count = self._get_item_count()
        values_ = {
            'title': u't\u00eftle {0}',
            'artist': u'the \u00e4rtist',
            'album': u'the \u00e4lbum',
            'track': item_count,
            'format': 'MP3',
        }
        values_.update(values)
        values_['title'] = values_['title'].format(item_count)
        values_['db'] = self.lib
        item = Item(**values_)
        if 'path' not in values:
            item['path'] = 'audio.' + item['format'].lower()
        return item

    def add_item(self, **values):
        """Add an item to the library and return it.

        Creates the item by passing the parameters to `create_item()`.

        If `path` is not set in `values` it is set to `item.destination()`.
        """
        # When specifying a path, store it normalized (as beets does
        # ordinarily).
        if 'path' in values:
            values['path'] = util.normpath(values['path'])

        item = self.create_item(**values)
        item.add(self.lib)

        # Ensure every item has a path.
        if 'path' not in values:
            item['path'] = item.destination()
            item.store()

        return item

    def add_album(self, **values):
        item = self.add_item(**values)
        return self.lib.add_album([item])

    def _get_item_count(self):
        if not hasattr(self, '__item_count'):
            count = 0
        return count

    # Running beets commands

    # Safe file operations

    def create_temp_dir(self):
        """Create a temporary directory and assign it into
        `self.temp_dir`. Call `remove_temp_dir` later to delete it.
        """
        temp_dir = mkdtemp()
        self.temp_dir = util.bytestring_path(temp_dir)

    def remove_temp_dir(self):
        """Delete the temporary directory created by `create_temp_dir`.
        """
        shutil.rmtree(self.temp_dir)


class TestImportSession(importer.ImportSession):
    """ImportSession that can be controlled programaticaly.

    >>> lib = Library(':memory:')
    >>> importer = TestImportSession(lib, paths=['/path/to/import'])
    >>> importer.add_choice(importer.action.SKIP)
    >>> importer.add_choice(importer.action.ASIS)
    >>> importer.default_choice = importer.action.APPLY
    >>> importer.run()

    This imports ``/path/to/import`` into `lib`. It skips the first
    album and imports thesecond one with metadata from the tags. For the
    remaining albums, the metadata from the autotagger will be applied.
    """

    def __init__(self, *args, **kwargs):
        super(TestImportSession, self).__init__(*args, **kwargs)
