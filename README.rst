.. image:: http://img.shields.io/pypi/v/phrydy.svg
    :target: https://pypi.python.org/pypi/phrydy

.. image:: https://travis-ci.org/Josef-Friedrich/phrydy.svg?branch=master
    :target: https://travis-ci.org/Josef-Friedrich/phrydy

======
phrydy
======

This package originates from the file `beets/mediafile.py <mediafile.py https://github.com/beetbox/beets/blob/master/beets/mediafile.py>`_
of the `beets project <http://beets.io>`_.

Handles low-level interfacing for files’ tags. Wraps Mutagen to
automatically detect file types and provide a unified interface for a
useful subset of music files’ tags.

Usage
-----

::

        >>> from phrydy install MediaFile
        >>> f = MediaFile('Lucy.mp3')
        >>> f.title
        u'Lucy in the Sky with Diamonds'
        >>> f.artist = 'The Beatles'
        >>> f.save()

A field will always return a reasonable value of the correct type, even
if no tag is present. If no value is available, the value will be false
(e.g., zero or the empty string).

Internally `MediaFile` uses `MediaField` descriptors to access the
data from the tags. In turn `MediaField` uses a number of
`StorageStyle` strategies to handle format specific logic.
