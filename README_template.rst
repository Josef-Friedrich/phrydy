{{ badge.pypi }}
{{ badge.github_workflow() }}
{{ badge.readthedocs }}

======
phrydy
======

This is an extended version of the
`mediafile <https://github.com/beetbox/mediafile>`_ library of the
`beets <https://beets.io>`_ project.
It is used by the Python audio renaming command line tool
`audiorename <https://github.com/Josef-Friedrich/audiorename>`_.

The name ``phrydy`` is pronounced like the German word ``Friedi``.

``phrydy`` offeres two media file classes: ``MediaFile`` is the unmodified
version that comes directly from the beets project. ``MediaFileExtended`` is the
slightly modified and extended version:

Changed fields:
---------------

- ``albumartist_sort``: Uses TSO2 Uses MP3s’ storage style ``TSO2``.
- ``composer_sort``: Uses MP3s’ description storage style ``composersortorder``.
- ``mb_workid``: Uses the additional storage style ``musicbrainz work id``.

New fields:
-----------

- ``mb_workhierarchy_ids``: All IDs in the work hierarchy.
- ``work``: The last work in the work hierarchy.
- ``work_hierarchy``: The hierarchy of works: The top level work appears first.
- ``releasegroup_types``: All items in the MusicBrainz’ API related to type: ``type``, ``primary-type`` and``secondary-type-list``.

Type hints:
-----------

``phrydy`` provides type hints:

.. image:: https://raw.githubusercontent.com/Josef-Friedrich/phrydy/refs/heads/main/docs/Type-hints.gif
    :alt: Type-hints.gif

Other additions:
----------------

- A little command line debug utility named ``phrydy-debug``.
- A dictionary containing documentation about the various meta data
  fields.
- Some code to generate documentation from the field documentation
  dictionary.

Installation
============

From PyPI
---------

.. code:: Shell

    pip install phrydy

From Github
------------

.. code:: Shell

    git clone git@github.com:Josef-Friedrich/phrydy.git
    cd phrydy
    pip install .

Usage
=====

Basic usage:

::

    >>> from phrydy import MediaFileExtended
    >>> f = MediaFileExtended('Lucy.mp3')
    >>> f.title
    'Lucy in the Sky with Diamonds'
    >>> f.artist = 'The Beatles'
    >>> f.save()

List all available fields of a media file:

.. code:: Python

    from phrydy import MediaFileExtended

    media_file = MediaFileExtended('tests/files/full.mp3')

    for key in MediaFileExtended.readable_fields():
        value = getattr(media_file, key)
        if key != 'art' and value:
            print('{}: {}'.format(key, value))

{{ func('phrydy.doc_generator.format_fields_as_rst_table') }}

phrydy-debug
============

{{ cli('phrydy-debug --help') | literal }}
