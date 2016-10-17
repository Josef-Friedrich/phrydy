# -*- coding: utf-8 -*-

import textwrap

fields = {
    # Ordinary metadata:
    'description': {
        'description': 'description',
        'category': 'ordinary',
    },
    'artist': {
        'description': 'artist',
        'category': 'ordinary',
    },
    'artist_sort': {
        'description': 'The “sort name” of the track artist (e.g., “Beatles, ' +
                 'The” or “White, Jack”)',
        'category': 'ordinary',
    },
    'artist_credit': {
        'description': 'The track-specific artist credit name,  which may be a ' +
                 'variation of the artist’s “canonical” name',
        'category': 'ordinary',
    },
    'album': {
        'description': 'album',
        'category': 'ordinary',
    },
    'albumartist': {
        'description': 'The artist for the entire album, which may be different ' +
                 'from the artists for the individual tracks',
        'category': 'ordinary',
    },
    'albumartist_sort': {
        'description': 'albumartist_sort',
        'category': 'ordinary',
    },
    'albumartist_credit': {
        'description': 'albumartist_credit',
        'category': 'ordinary',
    },
    'genre': {
        'description': 'genre',
        'category': 'ordinary',
    },
    'composer': {
        'description': 'composer',
        'category': 'ordinary',
    },
    'grouping': {
        'description': 'grouping',
        'category': 'ordinary',
    },
    # Separator
    'year': {
        'description': 'The release year of the specific release',
        'category': 'ordinary',
    },
    'month': {
        'description': 'The release month of the specific release',
        'category': 'ordinary',
    },
    'day': {
        'description': 'The release day of the specific release',
        'category': 'ordinary',
    },
    'original_year': {
        'description': 'The release year of the original version of the album',
        'category': 'ordinary',
    },
    'original_month': {
        'description': 'The release month of the original version of the album',
        'category': 'ordinary',
    },
    'original_day': {
        'description': 'The release day of the original version of the album',
        'category': 'ordinary',
    },
    # Separator
    'track': {
        'description': 'track',
        'category': 'ordinary',
    },
    'tracktotal': {
        'description': 'tracktotal',
        'category': 'ordinary',
    },
    'disc': {
        'description': 'disc',
        'category': 'ordinary',
    },
    'disctotal': {
        'description': 'disctotal',
        'category': 'ordinary',
    },
    # Separator
    'lyrics': {
        'description': 'lyrics',
        'category': 'ordinary',
    },
    'comments': {
        'description': 'comments',
        'category': 'ordinary',
    },
    'bpm': {
        'description': 'bpm',
        'category': 'ordinary',
    },
    'comp': {
        'description': 'Compilation flag',
        'category': 'ordinary',
    },
    'albumtype': {
        'description': 'The MusicBrainz album type; the MusicBrainz wiki has a ' +
                 'list of type names',
        'category': 'ordinary',
    },
    # Release
    'label': {
        'description': 'The label which issued the release. There may be more ' +
                 'than one.',
        'category': 'ordinary',
    },
    'asin': {
        'description': 'Amazon Standard Identification Number',
        'category': 'ordinary',
    },
    'catalognum': {
        'description': 'This is a number assigned to the release by the label ' +
                 'which can often be found on the spine or near the ' +
                 'barcode. There may be more than one, especially when ' +
                 'multiple labels are involved. This is not the ASIN — ' +
                 'there is a relationship for that — nor the label code.',
        'category': 'ordinary',
    },
    'script': {
        'description': 'The script used to write the release’s track list. The ' +
                 'possible values are taken from the ISO 15924 standard.',
        'category': 'ordinary',
    },
    'language': {
        'description': 'The language a release’s track list is written in. The ' +
                 'possible values are taken from the ISO 639-3 standard.',
        'category': 'ordinary',
    },
    'country': {
        'description': 'The country the release was issued in.',
        'category': 'ordinary',
    },
    'albumstatus': {
        'description': 'The status describes how "official" a release is. ' +
                 'Possible values are: official, promotional, bootleg, ' +
                 'pseudo-release',
        'category': 'ordinary',
    },
    'media': {
        'description': 'media',
        'category': 'ordinary',
    },
    'albumdisambig': {
        'description': 'albumdisambig',
        'category': 'ordinary',
    },
    'disctitle': {
        'description': 'disctitle',
        'category': 'ordinary',
    },
    'encoder': {
        'description': 'encoder',
        'category': 'ordinary',
    },
    # Audio information:
    'length': {
        'description': 'in seconds',
        'category': 'audio',
    },
    'bitrate': {
        'description': 'in kilobits per second, with units: e.g., “192kbps”',
        'category': 'audio',
    },
    'format': {
        'description': 'e.g., “MP3” or “FLAC”',
        'category': 'audio',
    },
    'channels': {
        'description': 'channels',
        'category': 'audio',
    },
    'bitdepth': {
        'description': 'only available for some formats',
        'category': 'audio',
    },
    'samplerate': {
        'description': 'in kilohertz, with units: e.g., “48kHz”',
        'category': 'audio',
    },
    # MusicBrainz and fingerprint information:
    'mb_trackid': {
        'description': 'MusicBrainz track ID',
        'category': 'music_brainz',
    },
    'mb_albumid': {
        'description': 'MusicBrainz album ID',
        'category': 'music_brainz',
    },
    'mb_artistid': {
        'description': 'MusicBrainz artist ID',
        'category': 'music_brainz',
    },
    'mb_albumartistid': {
        'description': 'MusicBrainz album artist ID',
        'category': 'music_brainz',
    },
    'mb_releasegroupid': {
        'description': 'MusicBrainz releasegroup  ID',
        'category': 'music_brainz',
    },
    'acoustid_fingerprint': {
        'description': 'Acoustic ID fingerprint',
        'category': 'music_brainz',
    },
    'acoustid_id': {
        'description': 'Acoustic ID',
        'category': 'music_brainz',
    },
}
"""
A multidimensional dictionary documenting all metadata fields.

.. code-block:: python

    fields = {
        'field': {
            'description': 'Title',
            'category': 'Category',
        },
    }
"""


def get_max_field_length(fields):
    """Get the length of the longest field in the dictionary ``fields``.

    :param dict fields: A dictionary to search for the longest field.
    """
    return max(map(len, fields))


def get_doc(additional_doc=False, field_prefix='$', field_suffix=':', indent=4):
    """Return a formated string containing documentation about the audio
    fields.
    """
    if additional_doc:
        f = fields.copy()
        f.update(additional_doc)
    else:
        f = fields
    field_length = get_max_field_length(f)
    field_length = field_length + len(field_prefix) + len(field_suffix) + 1
    description_indent = ' ' * (indent + field_length)
    output = ''
    for field, description in sorted(f.items()):
        description = description['description']
        field = ' ' * indent + field_prefix + field + ':'
        output += field.ljust(field_length) + \
            textwrap.fill(
                description,
                width=60,
                initial_indent=description_indent,
                subsequent_indent=description_indent
            )[field_length:] + '\n\n\n'

    return output
