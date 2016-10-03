# -*- coding: utf-8 -*-

fields = {
    # Ordinary metadata:
    'title': {
        'title': 'title',
        'category': 'ordinary',
    },
    'artist': {
        'title': 'artist',
        'category': 'ordinary',
    },
    'artist_sort': {
        'title': 'The “sort name” of the track artist (e.g., “Beatles, ' +
                 'The” or “White, Jack”)',
        'category': 'ordinary',
    },
    'artist_credit': {
        'title': 'The track-specific artist credit name,  which may be a ' +
                 'variation of the artist’s “canonical” name',
        'category': 'ordinary',
    },
    'album': {
        'title': 'album',
        'category': 'ordinary',
    },
    'albumartist': {
        'title': 'The artist for the entire album, which may be different ' +
                 'from the artists for the individual tracks',
        'category': 'ordinary',
    },
    'albumartist_sort': {
        'title': 'albumartist_sort',
        'category': 'ordinary',
    },
    'albumartist_credit': {
        'title': 'albumartist_credit',
        'category': 'ordinary',
    },
    'genre': {
        'title': 'genre',
        'category': 'ordinary',
    },
    'composer': {
        'title': 'composer',
        'category': 'ordinary',
    },
    'grouping': {
        'title': 'grouping',
        'category': 'ordinary',
    },
    # Separator
    'year': {
        'title': 'The release year of the specific release',
        'category': 'ordinary',
    },
    'month': {
        'title': 'The release month of the specific release',
        'category': 'ordinary',
    },
    'day': {
        'title': 'The release day of the specific release',
        'category': 'ordinary',
    },
    'original_year': {
        'title': 'The release year of the original version of the album',
        'category': 'ordinary',
    },
    'original_month': {
        'title': 'The release month of the original version of the album',
        'category': 'ordinary',
    },
    'original_day': {
        'title': 'The release day of the original version of the album',
        'category': 'ordinary',
    },
    # Separator
    'track': {
        'title': 'track',
        'category': 'ordinary',
    },
    'tracktotal': {
        'title': 'tracktotal',
        'category': 'ordinary',
    },
    'disc': {
        'title': 'disc',
        'category': 'ordinary',
    },
    'disctotal': {
        'title': 'disctotal',
        'category': 'ordinary',
    },
    # Separator
    'lyrics': {
        'title': 'lyrics',
        'category': 'ordinary',
    },
    'comments': {
        'title': 'comments',
        'category': 'ordinary',
    },
    'bpm': {
        'title': 'bpm',
        'category': 'ordinary',
    },
    'comp': {
        'title': 'Compilation flag',
        'category': 'ordinary',
    },
    'albumtype': {
        'title': 'The MusicBrainz album type; the MusicBrainz wiki has a ' +
                 'list of type names',
        'category': 'ordinary',
    },
    # Release
    'label': {
        'title': 'The label which issued the release. There may be more ' +
                 'than one.',
        'category': 'ordinary',
    },
    'asin': {
        'title': 'Amazon Standard Identification Number',
        'category': 'ordinary',
    },
    'catalognum': {
        'title': 'This is a number assigned to the release by the label ' +
                 'which can often be found on the spine or near the ' +
                 'barcode. There may be more than one, especially when ' +
                 'multiple labels are involved. This is not the ASIN — ' +
                 'there is a relationship for that — nor the label code.',
        'category': 'ordinary',
    },
    'script': {
        'title': 'The script used to write the release’s track list. The ' +
                 'possible values are taken from the ISO 15924 standard.',
        'category': 'ordinary',
    },
    'language': {
        'title': 'The language a release’s track list is written in. The ' +
                 'possible values are taken from the ISO 639-3 standard.',
        'category': 'ordinary',
    },
    'country': {
        'title': 'The country the release was issued in.',
        'category': 'ordinary',
    },
    'albumstatus': {
        'title': 'The status describes how "official" a release is. ' +
                 'Possible values are: official, promotional, bootleg, ' +
                 'pseudo-release',
        'category': 'ordinary',
    },
    'media': {
        'title': 'media',
        'category': 'ordinary',
    },
    'albumdisambig': {
        'title': 'albumdisambig',
        'category': 'ordinary',
    },
    'disctitle': {
        'title': 'disctitle',
        'category': 'ordinary',
    },
    'encoder': {
        'title': 'encoder',
        'category': 'ordinary',
    },
    # Audio information:
    'length': {
        'title': 'in seconds',
        'category': 'audio',
    },
    'bitrate': {
        'title': 'in kilobits per second, with units: e.g., “192kbps”',
        'category': 'audio',
    },
    'format': {
        'title': 'e.g., “MP3” or “FLAC”',
        'category': 'audio',
    },
    'channels': {
        'title': 'channels',
        'category': 'audio',
    },
    'bitdepth': {
        'title': 'only available for some formats',
        'category': 'audio',
    },
    'samplerate': {
        'title': 'in kilohertz, with units: e.g., “48kHz”',
        'category': 'audio',
    },
    # MusicBrainz and fingerprint information:
    'mb_trackid': {
        'title': 'MusicBrainz track ID',
        'category': 'music_brainz',
    },
    'mb_albumid': {
        'title': 'MusicBrainz album ID',
        'category': 'music_brainz',
    },
    'mb_artistid': {
        'title': 'MusicBrainz artist ID',
        'category': 'music_brainz',
    },
    'mb_albumartistid': {
        'title': 'MusicBrainz album artist ID',
        'category': 'music_brainz',
    },
    'mb_releasegroupid': {
        'title': 'MusicBrainz releasegroup  ID',
        'category': 'music_brainz',
    },
    'acoustid_fingerprint': {
        'title': 'Acoustic ID fingerprint',
        'category': 'music_brainz',
    },
    'acoustid_id': {
        'title': 'Acoustic ID',
        'category': 'music_brainz',
    },
}
"""
A multidimensional dictionary documenting all metadata fields.

.. code-block:: python

    fields = {
        'key': {
            'title': 'Title',
            'category': 'Category',
        },
    }
"""


def get_max_key_length(fields):
    """Get the length of the longest key in the dictionary ``fields``.

    :param dict fields: A dictionary to search for the longest key.
    """
    return max(map(len, fields))


def get_doc():
    """Return a formated string containing documentation about the audio
    fields.
    """
    key_length = get_max_key_length(fields)
    output = ''
    for key, value in fields.items():
        key = key + ':'
        output += key.ljust(key_length + 1 + 2) + value['title'] + '\n'

    return output
