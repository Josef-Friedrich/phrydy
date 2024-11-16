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

In the previous versions the ``phrydy`` library offers a standalone
version of the ``mediafile.py`` included in the ``beets`` project. Now
``beets`` has its own separate library called ``mediafile``. It might be
better to use the upstream library directly.

.. image:: https://raw.githubusercontent.com/Josef-Friedrich/phrydy/refs/heads/main/docs/Type-hints.gif
    :alt: Type-hints.gif

``phrydy`` offeres two media file classes: ``MediaFile`` is the
looped through and unmodified version that comes directly from the beets
project. ``MediaFileExtended`` is the slightly modified and extended
version:

Changed fields:
---------------

- ``albumartist_sort``
- ``composer_sort``
- ``mb_workid``

New fields:
-----------

- ``work``
- ``work_hierarchy``
- ``releasegroup_types``

Other additions:
----------------

- A little command line debug utility named ``phrydy-debug``.
- A dictionary containing documentation about the various meta data
  fields.
- Some code to generate documentation from the field documentation
  dictionary.

Installation
============

From Github
------------

.. code:: Shell

    git clone git@github.com:Josef-Friedrich/phrydy.git
    cd phrydy
    python setup.py install

From PyPI
----------

.. code:: Shell

    pip install phrydy
    easy_install phrydy

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

Development
===========

Test
----

::

    pyenv install 3.9.12 3.10.4
    pyenv local 3.9.12 3.10.4
    pip3 install tox tox-pyenv
    tox


Publish a new version
---------------------

::

    git tag 1.1.1
    git push --tags
    python setup.py sdist upload


Package documentation
---------------------

The package documentation is hosted on
`readthedocs <http://phrydy.readthedocs.io>`_.

Generate the package documentation:

::

    python setup.py build_sphinx
