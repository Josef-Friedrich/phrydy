Welcome to phrydy's documentation!
==================================

Contents:

.. toctree::
   :maxdepth: 2

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Handles low-level interfacing for files' tags. Wraps Mutagen to
automatically detect file types and provide a unified interface for a
useful subset of music files' tags.

Usage
-----

::

        >>> from phrydy install MediaFile
        >>> f = MediaFile('Lucy.mp3')
        >>> f.title
        'Lucy in the Sky with Diamonds'
        >>> f.artist = 'The Beatles'
        >>> f.save()

A field will always return a reasonable value of the correct type, even
if no tag is present. If no value is available, the value will be false
(e.g., zero or the empty string).

Internally `MediaFile` uses `MediaField` descriptors to access the
data from the tags. In turn `MediaField` uses a number of
`StorageStyle` strategies to handle format specific logic.
