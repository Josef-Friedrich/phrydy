.. image:: http://img.shields.io/pypi/v/phrydy.svg
    :target: https://pypi.python.org/pypi/phrydy
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/phrydy/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/phrydy/actions/workflows/tests.yml
    :alt: tests

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

In the previous versions the ``phrydy`` library offers a standalone
version of the ``mediafile.py`` included in the ``beets`` project. Now
``beets`` has its own separate library called ``mediafile``. It might be
better to use the upstream library directly.

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
     - The disambiguation album field helps to distinguish between identically named albums. The album “Weezer” for example has the disambiguation comments “Red Album” and “Green Album”.
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
     - A musician who creates arrangements.
     - 
   * - art
     - common
     - Legacy album art field.
     - ``b'\xff\xd8\xff\xe0\x00'``
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
     - ``['a-ha']``, ``['Anouk', 'Remon Stotijn']``
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
     - ``436523``, ``256000``
   * - bitrate_mode
     - common
     - bitrate_mode
     - ``CBR``
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
     - ``1``, ``2``
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
     - ``NL``
   * - date
     - date
     - The release data of the specific release.
     - ``1996-01-01``
   * - day
     - date
     - The release day of the specific release.
     - 
   * - disc
     - common
     - disc
     - ``1``
   * - disctitle
     - common
     - disctitle
     - 
   * - disctotal
     - common
     - disctotal
     - ``1``
   * - encoder
     - common
     - the name of the person or organisation that encoded the audio file. This field may contain a copyright message, if the audio file also is copyrighted by the encoder.
     - ``iTunes v7.6.2``
   * - encoder_info
     - common
     - encoder_info
     - ``LAME 3.92.0+``
   * - encoder_settings
     - common
     - encoder_settings
     - ``-b 255+``
   * - format
     - audio
     - e.g., “MP3” or “FLAC”
     - ``MP3``, ``FLAC``
   * - genre
     - common
     - genre
     - ``Rock``
   * - genres
     - common
     - genres
     - ``['Rock']``
   * - grouping
     - common
     - A content group, which is a collection of media items such as a CD boxed set.
     - 
   * - images
     - common
     - images
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
   * - length
     - audio
     - The length of a recording in seconds.
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
     - MusicBrainz album ID.
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
     - ``11``
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
     - The release year of the specific release.
     - ``2001``

phrydy-debug
============

:: 

    usage: phrydy-debug [-h] [-c] [-v] audio_file

    Debugging tool of the Python package “phrydy”, an easy wrapper around the “mutagen” library.

        [0;0;36macoustid_fingerprint[0;0m:    Acoustic ID fingerprint

        [0;0;36macoustid_id[0;0m:             Acoustic ID
                                 [0;0;33mExamples:[0;0m ['86e217b7-d3ad-4493-a9f2-cf71256ace07']

        [0;0;36malbum[0;0m:                   album
                                 [0;0;33mExamples:[0;0m ['Help!']

        [0;0;36malbumartist[0;0m:             The artist for the entire album, which may be
                                 different from the artists for the individual
                                 tracks
                                 [0;0;33mExamples:[0;0m ['The Beatles']

        [0;0;36malbumartist_credit[0;0m:      albumartist_credit

        [0;0;36malbumartist_sort[0;0m:        albumartist_sort
                                 [0;0;33mExamples:[0;0m ['Beatles, The']

        [0;0;36malbumartists[0;0m:            albumartists

        [0;0;36malbumdisambig[0;0m:           The disambiguation album field helps to
                                 distinguish between identically named albums. The
                                 album “Weezer” for example has the disambiguation
                                 comments “Red Album” and “Green Album”.

        [0;0;36malbumstatus[0;0m:             The status describes how "official" a release is.
                                 [0;0;33mExamples:[0;0m ['official', 'promotional', 'bootleg', 'pseudo-release']

        [0;0;36malbumtype[0;0m:               The MusicBrainz album type; the MusicBrainz wiki
                                 has a list of type names
                                 [0;0;33mExamples:[0;0m ['album/soundtrack']

        [0;0;36marranger[0;0m:                A musician who creates arrangements.

        [0;0;36mart[0;0m:                     Legacy album art field.
                                 [0;0;33mExamples:[0;0m [b'\xff\xd8\xff\xe0\x00']

        [0;0;36martist[0;0m:                  artist
                                 [0;0;33mExamples:[0;0m ['The Beatles']

        [0;0;36martist_credit[0;0m:           The track-specific artist credit name, which may
                                 be a variation of the artist’s “canonical” name

        [0;0;36martist_sort[0;0m:             The “sort name” of the track artist.
                                 [0;0;33mExamples:[0;0m ['Beatles, The', 'White, Jack']

        [0;0;36martists[0;0m:                 artists
                                 [0;0;33mExamples:[0;0m [['a-ha'], ['Anouk', 'Remon Stotijn']]

        [0;0;36masin[0;0m:                    Amazon Standard Identification Number
                                 [0;0;33mExamples:[0;0m ['B000002UAL']

        [0;0;36mbarcode[0;0m:                 There are many different types of barcode, but
                                 the ones usually found on music releases are two:
                                 1. Universal Product Code (UPC), which is the
                                 original barcode used in North America. 2.
                                 European Article Number (EAN)
                                 [0;0;33mExamples:[0;0m ['5028421931838', '036000291452']

        [0;0;36mbitdepth[0;0m:                only available for some formats
                                 [0;0;33mExamples:[0;0m [16]

        [0;0;36mbitrate[0;0m:                 in kilobits per second, with units: e.g.,
                                 “192kbps”
                                 [0;0;33mExamples:[0;0m [436523, 256000]

        [0;0;36mbitrate_mode[0;0m:            bitrate_mode
                                 [0;0;33mExamples:[0;0m ['CBR']

        [0;0;36mbpm[0;0m:                     Beats per Minute

        [0;0;36mcatalognum[0;0m:              This is a number assigned to the release by the
                                 label which can often be found on the spine or
                                 near the barcode. There may be more than one,
                                 especially when multiple labels are involved.
                                 This is not the ASIN — there is a relationship
                                 for that — nor the label code.
                                 [0;0;33mExamples:[0;0m ['CDP 7 46439 2']

        [0;0;36mchannels[0;0m:                channels
                                 [0;0;33mExamples:[0;0m [1, 2]

        [0;0;36mcomments[0;0m:                comments

        [0;0;36mcomp[0;0m:                    Compilation flag
                                 [0;0;33mExamples:[0;0m [True, False]

        [0;0;36mcomposer[0;0m:                The name of the composer.
                                 [0;0;33mExamples:[0;0m ['Ludwig van Beethoven']

        [0;0;36mcomposer_sort[0;0m:           The composer name for sorting.
                                 [0;0;33mExamples:[0;0m ['Beethoven, Ludwig van']

        [0;0;36mcopyright[0;0m:               copyright

        [0;0;36mcountry[0;0m:                 The country the release was issued in.
                                 [0;0;33mExamples:[0;0m ['NL']

        [0;0;36mdate[0;0m:                    The release data of the specific release.
                                 [0;0;33mExamples:[0;0m ['1996-01-01']

        [0;0;36mday[0;0m:                     The release day of the specific release.

        [0;0;36mdisc[0;0m:                    disc
                                 [0;0;33mExamples:[0;0m [1]

        [0;0;36mdisctitle[0;0m:               disctitle

        [0;0;36mdisctotal[0;0m:               disctotal
                                 [0;0;33mExamples:[0;0m [1]

        [0;0;36mencoder[0;0m:                 the name of the person or organisation that
                                 encoded the audio file. This field may contain a
                                 copyright message, if the audio file also is
                                 copyrighted by the encoder.
                                 [0;0;33mExamples:[0;0m ['iTunes v7.6.2']

        [0;0;36mencoder_info[0;0m:            encoder_info
                                 [0;0;33mExamples:[0;0m ['LAME 3.92.0+']

        [0;0;36mencoder_settings[0;0m:        encoder_settings
                                 [0;0;33mExamples:[0;0m ['-b 255+']

        [0;0;36mformat[0;0m:                  e.g., “MP3” or “FLAC”
                                 [0;0;33mExamples:[0;0m ['MP3', 'FLAC']

        [0;0;36mgenre[0;0m:                   genre
                                 [0;0;33mExamples:[0;0m ['Rock']

        [0;0;36mgenres[0;0m:                  genres
                                 [0;0;33mExamples:[0;0m [['Rock']]

        [0;0;36mgrouping[0;0m:                A content group, which is a collection of media
                                 items such as a CD boxed set.

        [0;0;36mimages[0;0m:                  images
                                 [0;0;33mExamples:[0;0m [['<mediafile.Image object at 0x7f51fce26b20>']]

        [0;0;36minitial_key[0;0m:             The Initial key frame contains the musical key in
                                 which the sound starts. It is represented as a
                                 string with a maximum length of three characters.
                                 The ground keys are represented with
                                 "A","B","C","D","E", "F" and "G" and halfkeys
                                 represented with "b" and "#". Minor is
                                 represented as "m".
                                 [0;0;33mExamples:[0;0m ['Dbm']

        [0;0;36misrc[0;0m:                    The International Standard Recording Code,
                                 abbreviated to ISRC, is a system of codes that
                                 identify audio and music video recordings.
                                 [0;0;33mExamples:[0;0m ['CAC118989003', 'ITO101117740']

        [0;0;36mlabel[0;0m:                   The label which issued the release. There may be
                                 more than one.
                                 [0;0;33mExamples:[0;0m ['Brilliant Classics', 'wea']

        [0;0;36mlanguage[0;0m:                The language a release’s track list is written
                                 in. The possible values are taken from the ISO
                                 639-3 standard.
                                 [0;0;33mExamples:[0;0m ['zxx', 'eng']

        [0;0;36mlength[0;0m:                  The length of a recording in seconds.
                                 [0;0;33mExamples:[0;0m [674.4666666666667]

        [0;0;36mlyricist[0;0m:                The writer of the text or lyrics in the
                                 recording.

        [0;0;36mlyrics[0;0m:                  The lyrics of the song or a text transcription of
                                 other vocal activities.

        [0;0;36mmb_albumartistid[0;0m:        MusicBrainz album artist ID.
                                 [0;0;33mExamples:[0;0m ['1f9df192-a621-4f54-8850-2c5373b7eac9', 'b972f589-fb0e-474e-b64a-803b0364fa75']

        [0;0;36mmb_albumartistids[0;0m:       MusicBrainz album artist IDs as a list.
                                 [0;0;33mExamples:[0;0m [['b972f589-fb0e-474e-b64a-803b0364fa75', 'dea28aa9-1086-4ffa-8739-0ccc759de1ce', 'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99']]

        [0;0;36mmb_albumid[0;0m:              MusicBrainz album ID.
                                 [0;0;33mExamples:[0;0m ['fd6adc77-1489-4a13-9aa0-32951061d92b']

        [0;0;36mmb_artistid[0;0m:             MusicBrainz artist ID.
                                 [0;0;33mExamples:[0;0m ['1f9df192-a621-4f54-8850-2c5373b7eac9']

        [0;0;36mmb_artistids[0;0m:            MusicBrainz artist IDs as a list.
                                 [0;0;33mExamples:[0;0m [['1f9df192-a621-4f54-8850-2c5373b7eac9']]

        [0;0;36mmb_releasegroupid[0;0m:       MusicBrainz releasegroup ID.
                                 [0;0;33mExamples:[0;0m ['f714fd70-aaca-4863-9d0d-2768a53acaeb']

        [0;0;36mmb_releasetrackid[0;0m:       MusicBrainz release track ID.
                                 [0;0;33mExamples:[0;0m ['38c8c114-5e3b-484f-8af0-79c47ef9c169']

        [0;0;36mmb_trackid[0;0m:              MusicBrainz track ID.
                                 [0;0;33mExamples:[0;0m ['c390b132-4a44-4e16-bec3-bffbbcaa19aa']

        [0;0;36mmb_workhierarchy_ids[0;0m:    All IDs in the work hierarchy. This field
                                 corresponds to the field `work_hierarchy`. The
                                 top level work ID appears first. A slash (/) is
                                 used as separator.
                                 [0;0;33mExamples:[0;0m ['e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / 5adc213f-700a-4435-9e95-831ed720f348 / eafec51f-47c5-3c66-8c36-a524246c85f8']

        [0;0;36mmb_workid[0;0m:               MusicBrainz work ID.
                                 [0;0;33mExamples:[0;0m ['508ec4b1-9549-38cd-a61e-1f0d120a6118']

        [0;0;36mmedia[0;0m:                   A prototypical medium is one of the physical,
                                 separate things you would get when you buy
                                 something in a record store.
                                 [0;0;33mExamples:[0;0m ['CD']

        [0;0;36mmonth[0;0m:                   The release month of the specific release.
                                 [0;0;33mExamples:[0;0m [11]

        [0;0;36moriginal_date[0;0m:           The release date of the original version of the
                                 album.
                                 [0;0;33mExamples:[0;0m ['1991-11-04']

        [0;0;36moriginal_day[0;0m:            The release day of the original version of the
                                 album.
                                 [0;0;33mExamples:[0;0m [4]

        [0;0;36moriginal_month[0;0m:          The release month of the original version of the
                                 album.
                                 [0;0;33mExamples:[0;0m [11]

        [0;0;36moriginal_year[0;0m:           The release year of the original version of the
                                 album.
                                 [0;0;33mExamples:[0;0m [1991]

        [0;0;36mr128_album_gain[0;0m:         An optional gain for album normalization. EBU R
                                 128 is a recommendation for loudness
                                 normalisation and maximum level of audio signals.

        [0;0;36mr128_track_gain[0;0m:         An optional gain for track normalization. EBU R
                                 128 is a recommendation for loudness
                                 normalisation and maximum level of audio signals.

        [0;0;36mreleasegroup_types[0;0m:      This field collects all items in the MusicBrainz’
                                 API  related to type: `type`, `primary-type and
                                 `secondary-type-list`. Main usage of this field
                                 is to determine in a secure manner if the release
                                 is a soundtrack.

        [0;0;36mrg_album_gain[0;0m:           ReplayGain Album Gain, see
                                 https://en.wikipedia.org/wiki/ReplayGain.

        [0;0;36mrg_album_peak[0;0m:           ReplayGain Album Peak, see
                                 https://en.wikipedia.org/wiki/ReplayGain.

        [0;0;36mrg_track_gain[0;0m:           ReplayGain Track Gain, see
                                 https://en.wikipedia.org/wiki/ReplayGain.
                                 [0;0;33mExamples:[0;0m [0.0]

        [0;0;36mrg_track_peak[0;0m:           ReplayGain Track Peak, see
                                 https://en.wikipedia.org/wiki/ReplayGain.
                                 [0;0;33mExamples:[0;0m [0.000244]

        [0;0;36msamplerate[0;0m:              The sample rate as an integer number.
                                 [0;0;33mExamples:[0;0m [44100]

        [0;0;36mscript[0;0m:                  The script used to write the release’s track
                                 list. The possible values are taken from the ISO
                                 15924 standard.
                                 [0;0;33mExamples:[0;0m ['Latn']

        [0;0;36mtitle[0;0m:                   The title of a audio file.
                                 [0;0;33mExamples:[0;0m ['32 Variations for Piano in C minor on an Original Theme, WoO 80']

        [0;0;36mtrack[0;0m:                   The track number.
                                 [0;0;33mExamples:[0;0m [1]

        [0;0;36mtracktotal[0;0m:              The total track number.
                                 [0;0;33mExamples:[0;0m [12]

        [0;0;36murl[0;0m:                     Uniform Resource Locator.

        [0;0;36mwork[0;0m:                    The Musicbrainzs’ work entity.
                                 [0;0;33mExamples:[0;0m ['32 Variations for Piano in C minor on an Original Theme, WoO 80']

        [0;0;36mwork_hierarchy[0;0m:          The hierarchy of works: The top level work
                                 appears first. As separator is this string used:
                                 -->.
                                 [0;0;33mExamples:[0;0m ['Die Zauberflöte, K. 620 --> Die Zauberflöte, K. 620: Akt I --> Die Zauberflöte, K. 620: Act I, Scene II. No. 2 Aria "Was hör ...']

        [0;0;36myear[0;0m:                    The release year of the specific release.
                                 [0;0;33mExamples:[0;0m [2001]

    positional arguments:
      audio_file     A audio file

    options:
      -h, --help     show this help message and exit
      -c, --color    Colorize the output
      -v, --version  show program's version number and exit

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
