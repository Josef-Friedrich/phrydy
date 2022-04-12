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
It is used by Python command line tool
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
   * - acoustid_fingerprint
     - music_brainz
     - Acoustic ID fingerprint
     - 
   * - acoustid_id
     - music_brainz
     - Acoustic ID
     - ``86e217b7-d3ad-4493-a9f2-cf71256ace07``
   * - album
     - common
     - album
     - ``Help!``
   * - albumartist
     - common
     - The artist for the entire album, which may be different from the artists for the individual tracks
     - ``The Beatles``
   * - albumartist_credit
     - common
     - albumartist_credit
     - 
   * - albumartist_sort
     - common
     - albumartist_sort
     - ``Beatles, The``
   * - albumartists
     - common
     - albumartists
     - 
   * - albumdisambig
     - common
     - albumdisambig
     - 
   * - albumstatus
     - common
     - The status describes how "official" a release is.
     - ``official``, ``promotional``, ``bootleg``, ``pseudo-release``
   * - albumtype
     - common
     - The MusicBrainz album type; the MusicBrainz wiki has a list of type names
     - ``album/soundtrack``
   * - arranger
     - common
     - arranger
     - 
   * - art
     - common
     - art
     - 
   * - artist
     - common
     - artist
     - ``The Beatles``
   * - artist_credit
     - common
     - The track-specific artist credit name, which may be a variation of the artist’s “canonical” name
     - 
   * - artist_sort
     - common
     - The “sort name” of the track artist.
     - ``Beatles, The``, ``White, Jack``
   * - artists
     - common
     - artists
     - 
   * - asin
     - common
     - Amazon Standard Identification Number
     - ``B000002UAL``
   * - barcode
     - common
     - There are many different types of barcode, but the ones usually found on music releases are two: 1. Universal Product Code (UPC), which is the original barcode used in North America. 2. European Article Number (EAN)
     - ``5028421931838``, ``036000291452``
   * - bitdepth
     - audio
     - only available for some formats
     - ``16``
   * - bitrate
     - audio
     - in kilobits per second, with units: e.g., “192kbps”
     - ``436523``
   * - bitrate_mode
     - common
     - bitrate_mode
     - 
   * - bpm
     - common
     - Beats per Minute
     - 
   * - catalognum
     - common
     - This is a number assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved. This is not the ASIN — there is a relationship for that — nor the label code.
     - ``CDP 7 46439 2``
   * - channels
     - audio
     - channels
     - ``1``
   * - comments
     - common
     - comments
     - 
   * - comp
     - common
     - Compilation flag
     - ``True``, ``False``
   * - composer
     - common
     - The name of the composer.
     - ``Ludwig van Beethoven``
   * - composer_sort
     - common
     - The composer name for sorting.
     - ``Beethoven, Ludwig van``
   * - copyright
     - common
     - copyright
     - 
   * - country
     - common
     - The country the release was issued in.
     - 
   * - date
     - date
     - date
     - 
   * - day
     - date
     - The release day of the specific release
     - 
   * - disc
     - common
     - disc
     - 
   * - disctitle
     - common
     - disctitle
     - 
   * - disctotal
     - common
     - disctotal
     - 
   * - encoder
     - common
     - the name of the person or organisation that encoded the audio file. This field may contain a copyright message, if the audio file also is copyrighted by the encoder.
     - ``iTunes v7.6.2``
   * - encoder_info
     - common
     - encoder_info
     - 
   * - encoder_settings
     - common
     - encoder_settings
     - 
   * - format
     - audio
     - e.g., “MP3” or “FLAC”
     - ``MP3``, ``FLAC``
   * - genre
     - common
     - genre
     - 
   * - genres
     - common
     - genres
     - 
   * - grouping
     - common
     - grouping
     - 
   * - images
     - common
     - images
     - 
   * - initial_key
     - common
     - The Initial key frame contains the musical key in which the sound starts. It is represented as a string with a maximum length of three characters. The ground keys are represented with "A","B","C","D","E", "F" and "G" and halfkeys represented with "b" and "#". Minor is represented as "m".
     - ``Dbm``
   * - isrc
     - common
     - The International Standard Recording Code, abbreviated to ISRC, is a system of codes that identify audio and music video recordings.
     - ``CAC118989003``, ``ITO101117740``
   * - label
     - common
     - The label which issued the release. There may be more than one.
     - ``Brilliant Classics``
   * - language
     - common
     - The language a release’s track list is written in. The possible values are taken from the ISO 639-3 standard.
     - ``zxx``
   * - length
     - audio
     - in seconds
     - ``674.4666666666667``
   * - lyricist
     - common
     - lyricist
     - 
   * - lyrics
     - common
     - lyrics
     - 
   * - mb_albumartistid
     - music_brainz
     - MusicBrainz album artist ID
     - ``1f9df192-a621-4f54-8850-2c5373b7eac9``, ``b972f589-fb0e-474e-b64a-803b0364fa75``
   * - mb_albumartistids
     - music_brainz
     - mb_albumartistids
     - ``['b972f589-fb0e-474e-b64a-803b0364fa75', 'dea28aa9-1086-4ffa-8739-0ccc759de1ce', 'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99']``
   * - mb_albumid
     - music_brainz
     - MusicBrainz album ID
     - ``fd6adc77-1489-4a13-9aa0-32951061d92b``
   * - mb_artistid
     - music_brainz
     - MusicBrainz artist ID
     - ``1f9df192-a621-4f54-8850-2c5373b7eac9``
   * - mb_artistids
     - music_brainz
     - mb_artistids
     - ``['1f9df192-a621-4f54-8850-2c5373b7eac9']``
   * - mb_releasegroupid
     - music_brainz
     - MusicBrainz releasegroup ID
     - ``f714fd70-aaca-4863-9d0d-2768a53acaeb``
   * - mb_releasetrackid
     - music_brainz
     - MusicBrainz release track ID
     - ``38c8c114-5e3b-484f-8af0-79c47ef9c169``
   * - mb_trackid
     - music_brainz
     - MusicBrainz track ID
     - ``c390b132-4a44-4e16-bec3-bffbbcaa19aa``
   * - mb_workhierarchy_ids
     - music_brainz
     - All IDs in the work hierarchy. This field corresponds to the field `work_hierarchy`. The top level work ID appears first. A slash (/) is used as separator.
     - ``e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / 5adc213f-700a-4435-9e95-831ed720f348 / eafec51f-47c5-3c66-8c36-a524246c85f8``
   * - mb_workid
     - music_brainz
     - MusicBrainz work ID
     - ``508ec4b1-9549-38cd-a61e-1f0d120a6118``
   * - media
     - common
     - media
     - ``CD``
   * - month
     - date
     - The release month of the specific release
     - 
   * - original_date
     - date
     - original_date
     - 
   * - original_day
     - date
     - The release day of the original version of the album
     - 
   * - original_month
     - date
     - The release month of the original version of the album
     - 
   * - original_year
     - date
     - The release year of the original version of the album
     - 
   * - r128_album_gain
     - rg
     - An optional gain for album normalization
     - 
   * - r128_track_gain
     - rg
     - An optional gain for track normalization
     - 
   * - releasegroup_types
     - music_brainz
     - This field collects all items in the MusicBrainz’ API  related to type: `type`, `primary-type and `secondary-type-list`. Main usage of this field is to determine in a secure manner if the release is a soundtrack.
     - 
   * - rg_album_gain
     - rg
     - ReplayGain Album Gain, see https://en.wikipedia.org/wiki/ReplayGain.
     - 
   * - rg_album_peak
     - rg
     - ReplayGain Album Peak, see https://en.wikipedia.org/wiki/ReplayGain.
     - 
   * - rg_track_gain
     - rg
     - ReplayGain Track Gain, see https://en.wikipedia.org/wiki/ReplayGain.
     - ``0.0``
   * - rg_track_peak
     - rg
     - ReplayGain Track Peak, see https://en.wikipedia.org/wiki/ReplayGain.
     - ``0.000244``
   * - samplerate
     - audio
     - in kilohertz, with units: e.g., “48kHz”
     - ``44100``
   * - script
     - common
     - The script used to write the release’s track list. The possible values are taken from the ISO 15924 standard.
     - ``Latn``
   * - title
     - common
     - The title of a audio file.
     - ``32 Variations for Piano in C minor on an Original Theme, WoO 80``
   * - track
     - common
     - The track number.
     - ``1``
   * - tracktotal
     - common
     - The total track number.
     - ``12``
   * - url
     - common
     - Uniform Resource Locator.
     - 
   * - work
     - common
     - The Musicbrainzs’ work entity.
     - ``32 Variations for Piano in C minor on an Original Theme, WoO 80``
   * - work_hierarchy
     - music_brainz
     - The hierarchy of works: The top level work appears first. As separator is this string used: -->.
     - ``Die Zauberflöte, K. 620 --> Die Zauberflöte, K. 620: Akt I --> Die Zauberflöte, K. 620: Act I, Scene II. No. 2 Aria "Was hör ...``
   * - year
     - date
     - The release year of the specific release
     - ``2001``



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
