.. image:: http://img.shields.io/pypi/v/phrydy.svg
    :target: https://pypi.python.org/pypi/phrydy
    :alt: This package on the Python Package Index

.. image:: https://readthedocs.org/projects/phrydy/badge/?version=latest
    :target: https://phrydy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

======
phrydy
======

This is a extended version of the
`mediafile <https://github.com/beetbox/mediafile>`_ library.
It is used by
`audiorename <https://github.com/Josef-Friedrich/audiorename>`_.

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
    u'Lucy in the Sky with Diamonds'
    >>> f.artist = 'The Beatles'
    >>> f.save()

List all available fields of a media file:

.. code:: Python

    from phrydy import MediaFileExtended

    media_file = MediaFileExtended('test/files/full.mp3')

    for key in MediaFileExtended.readable_fields():
        value = getattr(media_file, key)
        if key != 'art' and value:
            print('{}: {}'.format(key, value))


.. list-table:: Fields documentation
   :widths: 20 10 50 20
   :header-rows: 1

   * - Field name
     - Category
     - Description
     - Examples
   * - artist_sort
     - ordinary
     - The “sort name” of the track artist.
     - ``Beatles, The``, ``White, Jack``


Development
===========

Test
----

::

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
