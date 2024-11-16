.. image:: http://img.shields.io/pypi/v/phrydy.svg
    :target: https://pypi.org/project/phrydy
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/phrydy/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/phrydy/actions/workflows/tests.yml
    :alt: Tests

.. image:: https://readthedocs.org/projects/phrydy/badge/?version=latest
    :target: https://phrydy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

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

.. list-table:: Fields documentation
   :widths: 20 10 50 20
   :header-rows: 1

   * - Field name
     - Category
     - Description
     - Examples
   * - acoustid_fingerprint
     - music_brainz
     - The Acoustic Fingerprint for the track. The fingerprint is based on the audio information found in a file, and is calculated using the Chromaprint software.
     - 
   * - acoustid_id
     - music_brainz
     - The AcoustID associated with the track. The AcoustID is the identifier assigned to an audio file based on its acoustic fingerprint. Multiple fingerprints may be assigned the same AcoustID if the fingerprints are similar enough.
     - ``86e217b7-d3ad-4493-a9f2-cf71256ace07``
   * - album
     - common
     - The title of the release.
     - ``Help!``
   * - albumartist
     - common
     - The artist for the entire album, which may be different from the artists for the individual tracks. The artists primarily credited on the release, separated by the specified join phrases.
     - ``The Beatles``
   * - albumartist_credit
     - common
     - The release-specific artist credit name, which may be a variation of the artist’s “canonical” name.
     - 
   * - albumartist_sort
     - common
     - The release artists sort names, separated by the specified join phrases. (e.g.: “Beatles, The”).
     - ``Beatles, The``
   * - albumartists
     - common
     - The album artists specifed as a list.
     - ``['The Beatles']``
   * - albumartists_credit
     - common
     - The release-specific artists credit names, which may be a variation of the artist’s “canonical” names.
     - 
   * - albumartists_sort
     - common
     - The “sort name” of the artist for the entire album.
     - ``Beatles, The``, ``White, Jack``
   * - albumdisambig
     - common
     - The disambiguation album field helps to distinguish between identically named albums. The album “Weezer” for example has the disambiguation comments “Red Album” and “Green Album”.
     - 
   * - albumstatus
     - common
     - The status describes how "official" a release is.
     - ``official``, ``promotional``, ``bootleg``, ``pseudo-release``
   * - albumtype
     - common
     - The primary MusicBrainz release group type; the MusicBrainz wiki has a list of type names.
     - ``album/soundtrack``
   * - albumtypes
     - common
     - The MusicBrainz release group types; the MusicBrainz wiki has a list of type names.
     - ``['album', 'soundtrack']``
   * - arranger
     - common
     - A musician who creates arrangements.
     - 
   * - art
     - common
     - Legacy album art field.
     - ``b'\xff\xd8\xff\xe0\x00'``
   * - artist
     - common
     - The track artist names, separated by the specified join phrases.
     - ``The Beatles``
   * - artist_credit
     - common
     - The track-specific artist credit name, which may be a variation of the artist’s “canonical” name.
     - 
   * - artist_sort
     - common
     - The “sort name” of the track artist.
     - ``Beatles, The``, ``White, Jack``
   * - artists
     - common
     - A multi-value field containing the track artist names.
     - ``['a-ha']``, ``['Anouk', 'Remon Stotijn']``
   * - artists_credit
     - common
     - The track-specific artists credit names, which may be a variation of the artist’s “canonical” names.
     - 
   * - artists_sort
     - common
     - The “sort name” of the track artists.
     - ``['Beatles, The', 'White, Jack']``
   * - asin
     - common
     - The Amazon Standard Identification Number - the number identifying the item on Amazon.
     - ``B000002UAL``
   * - barcode
     - common
     - The barcode assigned to the release. There are many different types of barcode, but the ones usually found on music releases are two: 1. Universal Product Code (UPC), which is the original barcode used in North America. 2. European Article Number (EAN).
     - ``5028421931838``, ``036000291452``
   * - bitdepth
     - audio
     - The number of bits per sample in the audio encoding (an int). Only available for certain file formats (zero where unavailable).
     - ``16``
   * - bitrate
     - audio
     - The number of bits per seconds used in the audio coding (an int). If this is provided explicitly by the compressed file format, this is a precise reflection of the encoding. Otherwise, it is estimated from the on-disk file size. In this case, some imprecision is possible because the file header is incorporated in the file size.
     - ``436523``, ``256000``
   * - bitrate_mode
     - common
     - The mode of the bitrate used in the audio coding (a string, eg. "CBR", "VBR" or "ABR"). Only available for the MP3 file format (empty where unavailable).
     - ``CBR``
   * - bpm
     - common
     - The number of beats per minute of the track.
     - 
   * - catalognum
     - common
     - A number assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved.
     - ``CDP 7 46439 2``
   * - catalognums
     - common
     - Multiple numbers assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved.
     - ``['CDP 7 46439 2', 'Do 247282']``
   * - channels
     - audio
     - The number of channels in the audio (an int).
     - ``1``, ``2``
   * - comments
     - common
     - The disambiguation comment entered to help distinguish one release from another (e.g.: Deluxe version with 2 bonus tracks).
     - 
   * - comp
     - common
     - Compilation flag.
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
     - The copyright message for the copyright holder of the original sound, beginning with a year and a space character.
     - 
   * - country
     - common
     - The country the release was issued in.
     - ``NL``, ``EN``, ``GB``
   * - date
     - date
     - The release date of the specific release.
     - ``1996-01-01``
   * - day
     - date
     - The release day of the specific release.
     - ``31``
   * - disc
     - common
     - The number of the disc.
     - ``1``
   * - disctitle
     - common
     - Mediums are always included in a release, and have a position in said release (e.g. disc 1 or disc 2). They have a format, like CD, 12" vinyl or cassette (in some cases this will be unknown), and can have an optional title (e.g. disc 2: The Early Years).
     - ``disc 2: The Early Years``
   * - disctotal
     - common
     - The total number of discs.
     - ``1``
   * - encoder
     - common
     - The name of the person or organisation that encoded the audio file. This field may contain a copyright message, if the audio file also is copyrighted by the encoder.
     - ``iTunes v7.6.2``
   * - encoder_info
     - common
     - The name and/or version of the encoder used (a string, eg. "LAME 3.97.0"). Only available for some formats (empty where unavailable)
     - ``LAME 3.92.0+``
   * - encoder_settings
     - common
     - A guess of the settings used for the encoder (a string, eg. "-V2"). Only available for the MP3 file format (empty where unavailable).
     - ``-b 255+``
   * - format
     - audio
     - A string describing the file format/codec. e.g., “MP3” or “FLAC”
     - ``MP3``, ``FLAC``
   * - genre
     - common
     - Genres are currently supported in MusicBrainz as part of the tag system.
     - ``Rock``
   * - genres
     - common
     - Genres are currently supported in MusicBrainz as part of the tag system.
     - ``['Rock']``
   * - grouping
     - common
     - A content group, which is a collection of media items such as a CD boxed set.
     - 
   * - images
     - common
     - Cover art, also known as "album art" or "album artwork", is artwork that provides a visual representation of a release.
     - ``['<mediafile.Image object at 0x7f51fce26b20>']``
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
     - ``Brilliant Classics``, ``wea``
   * - language
     - common
     - The language a release’s track list is written in. The possible values are taken from the ISO 639-3 standard.
     - ``zxx``, ``eng``
   * - languages
     - common
     - The language a release’s track list is written in. The possible values are taken from the ISO 639-3 standard.
     - ``['zxx', 'eng']``
   * - length
     - audio
     - The duration of the audio in seconds (a float).
     - ``674.4666666666667``
   * - lyricist
     - common
     - The writer of the text or lyrics in the recording.
     - 
   * - lyrics
     - common
     - The lyrics of the song or a text transcription of other vocal activities.
     - 
   * - mb_albumartistid
     - music_brainz
     - MusicBrainz album artist ID.
     - ``1f9df192-a621-4f54-8850-2c5373b7eac9``, ``b972f589-fb0e-474e-b64a-803b0364fa75``
   * - mb_albumartistids
     - music_brainz
     - MusicBrainz album artist IDs as a list.
     - ``['b972f589-fb0e-474e-b64a-803b0364fa75', 'dea28aa9-1086-4ffa-8739-0ccc759de1ce', 'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99']``
   * - mb_albumid
     - music_brainz
     - MusicBrainz work ID.
     - ``fd6adc77-1489-4a13-9aa0-32951061d92b``
   * - mb_artistid
     - music_brainz
     - MusicBrainz artist ID.
     - ``1f9df192-a621-4f54-8850-2c5373b7eac9``
   * - mb_artistids
     - music_brainz
     - MusicBrainz artist IDs as a list.
     - ``['1f9df192-a621-4f54-8850-2c5373b7eac9']``
   * - mb_releasegroupid
     - music_brainz
     - MusicBrainz releasegroup ID.
     - ``f714fd70-aaca-4863-9d0d-2768a53acaeb``
   * - mb_releasetrackid
     - music_brainz
     - MusicBrainz release track ID.
     - ``38c8c114-5e3b-484f-8af0-79c47ef9c169``
   * - mb_trackid
     - music_brainz
     - MusicBrainz track ID.
     - ``c390b132-4a44-4e16-bec3-bffbbcaa19aa``
   * - mb_workhierarchy_ids
     - music_brainz
     - All IDs in the work hierarchy. This field corresponds to the field `work_hierarchy`. The top level work ID appears first. A slash (/) is used as separator.
     - ``e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / 5adc213f-700a-4435-9e95-831ed720f348 / eafec51f-47c5-3c66-8c36-a524246c85f8``
   * - mb_workid
     - music_brainz
     - MusicBrainz work ID.
     - ``508ec4b1-9549-38cd-a61e-1f0d120a6118``
   * - media
     - common
     - A prototypical medium is one of the physical, separate things you would get when you buy something in a record store.
     - ``CD``
   * - month
     - date
     - The release month of the specific release.
     - ``12``
   * - original_date
     - date
     - The release date of the original version of the album.
     - ``1991-11-04``
   * - original_day
     - date
     - The release day of the original version of the album.
     - ``4``
   * - original_month
     - date
     - The release month of the original version of the album.
     - ``11``
   * - original_year
     - date
     - The release year of the original version of the album.
     - ``1991``
   * - r128_album_gain
     - r128
     - An optional gain for album normalization. EBU R 128 is a recommendation for loudness normalisation and maximum level of audio signals.
     - 
   * - r128_track_gain
     - r128
     - An optional gain for track normalization. EBU R 128 is a recommendation for loudness normalisation and maximum level of audio signals.
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
     - The sample rate as an integer number.
     - ``44100``
   * - script
     - common
     - The script used to write the release’s track list. The possible values are taken from the ISO 15924 standard.
     - ``Latn``
   * - title
     - common
     - The title of the track.
     - ``32 Variations for Piano in C minor on an Original Theme, WoO 80``
   * - track
     - common
     - The number of the track on the disc.
     - ``1``
   * - tracktotal
     - common
     - The total number of tracks on this disc.
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
     - The release year of the specific release.
     - ``2001``

phrydy-debug
============

:: 

    usage: phrydy-debug [-h] [-c] [-v] audio_file

    Debugging tool of the Python package “phrydy”, an easy wrapper around the “mutagen” library.

        acoustid_fingerprint:    The Acoustic Fingerprint for the track. The
                                 fingerprint is based on the audio information
                                 found in a file, and is calculated using the
                                 Chromaprint software.

        acoustid_id:             The AcoustID associated with the track. The
                                 AcoustID is the identifier assigned to an audio
                                 file based on its acoustic fingerprint. Multiple
                                 fingerprints may be assigned the same AcoustID if
                                 the fingerprints are similar enough.
                                 Examples: ['86e217b7-d3ad-4493-a9f2-cf71256ace07']

        album:                   The title of the release.
                                 Examples: ['Help!']

        albumartist:             The artist for the entire album, which may be
                                 different from the artists for the individual
                                 tracks. The artists primarily credited on the
                                 release, separated by the specified join phrases.
                                 Examples: ['The Beatles']

        albumartist_credit:      The release-specific artist credit name, which
                                 may be a variation of the artist’s “canonical”
                                 name.

        albumartist_sort:        The release artists sort names, separated by the
                                 specified join phrases. (e.g.: “Beatles, The”).
                                 Examples: ['Beatles, The']

        albumartists:            The album artists specifed as a list.
                                 Examples: [['The Beatles']]

        albumartists_credit:     The release-specific artists credit names, which
                                 may be a variation of the artist’s “canonical”
                                 names.

        albumartists_sort:       The “sort name” of the artist for the entire
                                 album.
                                 Examples: ['Beatles, The', 'White, Jack']

        albumdisambig:           The disambiguation album field helps to
                                 distinguish between identically named albums. The
                                 album “Weezer” for example has the disambiguation
                                 comments “Red Album” and “Green Album”.

        albumstatus:             The status describes how "official" a release is.
                                 Examples: ['official', 'promotional', 'bootleg', 'pseudo-release']

        albumtype:               The primary MusicBrainz release group type; the
                                 MusicBrainz wiki has a list of type names.
                                 Examples: ['album/soundtrack']

        albumtypes:              The MusicBrainz release group types; the
                                 MusicBrainz wiki has a list of type names.
                                 Examples: [['album', 'soundtrack']]

        arranger:                A musician who creates arrangements.

        art:                     Legacy album art field.
                                 Examples: [b'\xff\xd8\xff\xe0\x00']

        artist:                  The track artist names, separated by the
                                 specified join phrases.
                                 Examples: ['The Beatles']

        artist_credit:           The track-specific artist credit name, which may
                                 be a variation of the artist’s “canonical” name.

        artist_sort:             The “sort name” of the track artist.
                                 Examples: ['Beatles, The', 'White, Jack']

        artists:                 A multi-value field containing the track artist
                                 names.
                                 Examples: [['a-ha'], ['Anouk', 'Remon Stotijn']]

        artists_credit:          The track-specific artists credit names, which
                                 may be a variation of the artist’s “canonical”
                                 names.

        artists_sort:            The “sort name” of the track artists.
                                 Examples: [['Beatles, The', 'White, Jack']]

        asin:                    The Amazon Standard Identification Number - the
                                 number identifying the item on Amazon.
                                 Examples: ['B000002UAL']

        barcode:                 The barcode assigned to the release. There are
                                 many different types of barcode, but the ones
                                 usually found on music releases are two: 1.
                                 Universal Product Code (UPC), which is the
                                 original barcode used in North America. 2.
                                 European Article Number (EAN).
                                 Examples: ['5028421931838', '036000291452']

        bitdepth:                The number of bits per sample in the audio
                                 encoding (an int). Only available for certain
                                 file formats (zero where unavailable).
                                 Examples: [16]

        bitrate:                 The number of bits per seconds used in the audio
                                 coding (an int). If this is provided explicitly
                                 by the compressed file format, this is a precise
                                 reflection of the encoding. Otherwise, it is
                                 estimated from the on-disk file size. In this
                                 case, some imprecision is possible because the
                                 file header is incorporated in the file size.
                                 Examples: [436523, 256000]

        bitrate_mode:            The mode of the bitrate used in the audio coding
                                 (a string, eg. "CBR", "VBR" or "ABR"). Only
                                 available for the MP3 file format (empty where
                                 unavailable).
                                 Examples: ['CBR']

        bpm:                     The number of beats per minute of the track.

        catalognum:              A number assigned to the release by the label
                                 which can often be found on the spine or near the
                                 barcode. There may be more than one, especially
                                 when multiple labels are involved.
                                 Examples: ['CDP 7 46439 2']

        catalognums:             Multiple numbers assigned to the release by the
                                 label which can often be found on the spine or
                                 near the barcode. There may be more than one,
                                 especially when multiple labels are involved.
                                 Examples: [['CDP 7 46439 2', 'Do 247282']]

        channels:                The number of channels in the audio (an int).
                                 Examples: [1, 2]

        comments:                The disambiguation comment entered to help
                                 distinguish one release from another (e.g.:
                                 Deluxe version with 2 bonus tracks).

        comp:                    Compilation flag.
                                 Examples: [True, False]

        composer:                The name of the composer.
                                 Examples: ['Ludwig van Beethoven']

        composer_sort:           The composer name for sorting.
                                 Examples: ['Beethoven, Ludwig van']

        copyright:               The copyright message for the copyright holder of
                                 the original sound, beginning with a year and a
                                 space character.

        country:                 The country the release was issued in.
                                 Examples: ['NL', 'EN', 'GB']

        date:                    The release date of the specific release.
                                 Examples: ['1996-01-01']

        day:                     The release day of the specific release.
                                 Examples: [31]

        disc:                    The number of the disc.
                                 Examples: [1]

        disctitle:               Mediums are always included in a release, and
                                 have a position in said release (e.g. disc 1 or
                                 disc 2). They have a format, like CD, 12" vinyl
                                 or cassette (in some cases this will be unknown),
                                 and can have an optional title (e.g. disc 2: The
                                 Early Years).
                                 Examples: ['disc 2: The Early Years']

        disctotal:               The total number of discs.
                                 Examples: [1]

        encoder:                 The name of the person or organisation that
                                 encoded the audio file. This field may contain a
                                 copyright message, if the audio file also is
                                 copyrighted by the encoder.
                                 Examples: ['iTunes v7.6.2']

        encoder_info:            The name and/or version of the encoder used (a
                                 string, eg. "LAME 3.97.0"). Only available for
                                 some formats (empty where unavailable)
                                 Examples: ['LAME 3.92.0+']

        encoder_settings:        A guess of the settings used for the encoder (a
                                 string, eg. "-V2"). Only available for the MP3
                                 file format (empty where unavailable).
                                 Examples: ['-b 255+']

        format:                  A string describing the file format/codec. e.g.,
                                 “MP3” or “FLAC”
                                 Examples: ['MP3', 'FLAC']

        genre:                   Genres are currently supported in MusicBrainz as
                                 part of the tag system.
                                 Examples: ['Rock']

        genres:                  Genres are currently supported in MusicBrainz as
                                 part of the tag system.
                                 Examples: [['Rock']]

        grouping:                A content group, which is a collection of media
                                 items such as a CD boxed set.

        images:                  Cover art, also known as "album art" or "album
                                 artwork", is artwork that provides a visual
                                 representation of a release.
                                 Examples: [['<mediafile.Image object at 0x7f51fce26b20>']]

        initial_key:             The Initial key frame contains the musical key in
                                 which the sound starts. It is represented as a
                                 string with a maximum length of three characters.
                                 The ground keys are represented with
                                 "A","B","C","D","E", "F" and "G" and halfkeys
                                 represented with "b" and "#". Minor is
                                 represented as "m".
                                 Examples: ['Dbm']

        isrc:                    The International Standard Recording Code,
                                 abbreviated to ISRC, is a system of codes that
                                 identify audio and music video recordings.
                                 Examples: ['CAC118989003', 'ITO101117740']

        label:                   The label which issued the release. There may be
                                 more than one.
                                 Examples: ['Brilliant Classics', 'wea']

        language:                The language a release’s track list is written
                                 in. The possible values are taken from the ISO
                                 639-3 standard.
                                 Examples: ['zxx', 'eng']

        languages:               The language a release’s track list is written
                                 in. The possible values are taken from the ISO
                                 639-3 standard.
                                 Examples: [['zxx', 'eng']]

        length:                  The duration of the audio in seconds (a float).
                                 Examples: [674.4666666666667]

        lyricist:                The writer of the text or lyrics in the
                                 recording.

        lyrics:                  The lyrics of the song or a text transcription of
                                 other vocal activities.

        mb_albumartistid:        MusicBrainz album artist ID.
                                 Examples: ['1f9df192-a621-4f54-8850-2c5373b7eac9', 'b972f589-fb0e-474e-b64a-803b0364fa75']

        mb_albumartistids:       MusicBrainz album artist IDs as a list.
                                 Examples: [['b972f589-fb0e-474e-b64a-803b0364fa75', 'dea28aa9-1086-4ffa-8739-0ccc759de1ce', 'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99']]

        mb_albumid:              MusicBrainz work ID.
                                 Examples: ['fd6adc77-1489-4a13-9aa0-32951061d92b']

        mb_artistid:             MusicBrainz artist ID.
                                 Examples: ['1f9df192-a621-4f54-8850-2c5373b7eac9']

        mb_artistids:            MusicBrainz artist IDs as a list.
                                 Examples: [['1f9df192-a621-4f54-8850-2c5373b7eac9']]

        mb_releasegroupid:       MusicBrainz releasegroup ID.
                                 Examples: ['f714fd70-aaca-4863-9d0d-2768a53acaeb']

        mb_releasetrackid:       MusicBrainz release track ID.
                                 Examples: ['38c8c114-5e3b-484f-8af0-79c47ef9c169']

        mb_trackid:              MusicBrainz track ID.
                                 Examples: ['c390b132-4a44-4e16-bec3-bffbbcaa19aa']

        mb_workhierarchy_ids:    All IDs in the work hierarchy. This field
                                 corresponds to the field `work_hierarchy`. The
                                 top level work ID appears first. A slash (/) is
                                 used as separator.
                                 Examples: ['e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / 5adc213f-700a-4435-9e95-831ed720f348 / eafec51f-47c5-3c66-8c36-a524246c85f8']

        mb_workid:               MusicBrainz work ID.
                                 Examples: ['508ec4b1-9549-38cd-a61e-1f0d120a6118']

        media:                   A prototypical medium is one of the physical,
                                 separate things you would get when you buy
                                 something in a record store.
                                 Examples: ['CD']

        month:                   The release month of the specific release.
                                 Examples: [12]

        original_date:           The release date of the original version of the
                                 album.
                                 Examples: ['1991-11-04']

        original_day:            The release day of the original version of the
                                 album.
                                 Examples: [4]

        original_month:          The release month of the original version of the
                                 album.
                                 Examples: [11]

        original_year:           The release year of the original version of the
                                 album.
                                 Examples: [1991]

        r128_album_gain:         An optional gain for album normalization. EBU R
                                 128 is a recommendation for loudness
                                 normalisation and maximum level of audio signals.

        r128_track_gain:         An optional gain for track normalization. EBU R
                                 128 is a recommendation for loudness
                                 normalisation and maximum level of audio signals.

        releasegroup_types:      This field collects all items in the MusicBrainz’
                                 API  related to type: `type`, `primary-type and
                                 `secondary-type-list`. Main usage of this field
                                 is to determine in a secure manner if the release
                                 is a soundtrack.

        rg_album_gain:           ReplayGain Album Gain, see
                                 https://en.wikipedia.org/wiki/ReplayGain.

        rg_album_peak:           ReplayGain Album Peak, see
                                 https://en.wikipedia.org/wiki/ReplayGain.

        rg_track_gain:           ReplayGain Track Gain, see
                                 https://en.wikipedia.org/wiki/ReplayGain.
                                 Examples: [0.0]

        rg_track_peak:           ReplayGain Track Peak, see
                                 https://en.wikipedia.org/wiki/ReplayGain.
                                 Examples: [0.000244]

        samplerate:              The sample rate as an integer number.
                                 Examples: [44100]

        script:                  The script used to write the release’s track
                                 list. The possible values are taken from the ISO
                                 15924 standard.
                                 Examples: ['Latn']

        title:                   The title of the track.
                                 Examples: ['32 Variations for Piano in C minor on an Original Theme, WoO 80']

        track:                   The number of the track on the disc.
                                 Examples: [1]

        tracktotal:              The total number of tracks on this disc.
                                 Examples: [12]

        url:                     Uniform Resource Locator.

        work:                    The Musicbrainzs’ work entity.
                                 Examples: ['32 Variations for Piano in C minor on an Original Theme, WoO 80']

        work_hierarchy:          The hierarchy of works: The top level work
                                 appears first. As separator is this string used:
                                 -->.
                                 Examples: ['Die Zauberflöte, K. 620 --> Die Zauberflöte, K. 620: Akt I --> Die Zauberflöte, K. 620: Act I, Scene II. No. 2 Aria "Was hör ...']

        year:                    The release year of the specific release.
                                 Examples: [2001]

    positional arguments:
      audio_file     A audio file

    options:
      -h, --help     show this help message and exit
      -c, --color    Colorize the output
      -v, --version  show program's version number and exit

