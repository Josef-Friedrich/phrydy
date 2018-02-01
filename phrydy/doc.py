# -*- coding: utf-8 -*-

import textwrap
from phrydy.utils import as_string
import ansicolor

fields = {
    # Ordinary metadata:
    'title': {
        'description': 'The title of a audio file.',
        'category': 'ordinary',
    },
    'arranger': {
        'description': 'arranger',
        'category': 'ordinary',
    },
    'art': {
        'description': 'art',
        'category': 'ordinary',
    },
    'initial_key': {
        'description': 'initial_key',
        'category': 'ordinary',
    },
    'images': {
        'description': 'images',
        'category': 'ordinary',
    },
    'artist': {
        'description': 'artist',
        'category': 'ordinary',
    },
    'artist_sort': {
        'description': 'The “sort name” of the track artist (e.g., ' +
                       '“Beatles, The” or “White, Jack”)',
        'category': 'ordinary',
    },
    'artist_credit': {
        'description': 'The track-specific artist credit name, which may ' +
                       'be a variation of the artist’s “canonical” name',
        'category': 'ordinary',
    },
    'album': {
        'description': 'album',
        'category': 'ordinary',
    },
    'albumartist': {
        'description': 'The artist for the entire album, which may be ' +
                       'different from the artists for the individual tracks',
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
    'genres': {
        'description': 'genres',
        'category': 'ordinary',
    },
    'composer': {
        'description': 'composer',
        'category': 'ordinary',
    },
    'composer_sort': {
        'description': 'Composer name for sorting.',
        'category': 'ordinary',
    },
    'grouping': {
        'description': 'grouping',
        'category': 'ordinary',
    },
    # Date
    'date': {
        'description': 'date',
        'category': 'date',
    },
    'year': {
        'description': 'The release year of the specific release',
        'category': 'date',
    },
    'month': {
        'description': 'The release month of the specific release',
        'category': 'date',
    },
    'day': {
        'description': 'The release day of the specific release',
        'category': 'date',
    },
    'original_date': {
        'description': 'original_date',
        'category': 'date',
    },
    'original_year': {
        'description': 'The release year of the original version of the album',
        'category': 'date',
    },
    'original_month': {
        'description': 'The release month of the original version of the ' +
                       'album',
        'category': 'date',
    },
    'original_day': {
        'description': 'The release day of the original version of the album',
        'category': 'date',
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
    'lyricist': {
        'description': 'lyricist',
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
        'description': 'The MusicBrainz album type; the MusicBrainz wiki ' +
                       'has a list of type names',
        'category': 'ordinary',
    },
    'releasegroup_types': {
        'description': 'This field collects all items in the MusicBrainz’ API '
                       ' related to type: `type`, `primary-type and '
                       '`secondary-type-list`. Main usage of this field is to '
                       'determine in a secure manner if the release is a '
                       'soundtrack.',
        'category': 'music_brainz',
    },
    # Release
    'label': {
        'description': 'The label which issued the release. There may be ' +
                       'more than one.',
        'category': 'ordinary',
    },
    'asin': {
        'description': 'Amazon Standard Identification Number',
        'category': 'ordinary',
    },
    'catalognum': {
        'description': 'This is a number assigned to the release by the ' +
                       'label which can often be found on the spine or near ' +
                       'the barcode. There may be more than one, especially ' +
                       'when multiple labels are involved. This is not the ' +
                       'ASIN — there is a relationship for that — nor the ' +
                       'label code.',
        'category': 'ordinary',
    },
    'script': {
        'description': 'The script used to write the release’s track list. ' +
                       'The possible values are taken from the ISO 15924 ' +
                       'standard.',
        'category': 'ordinary',
    },
    'language': {
        'description': 'The language a release’s track list is written in. ' +
                       'The possible values are taken from the ISO 639-3 ' +
                       'standard.',
        'category': 'ordinary',
    },
    'country': {
        'description': 'The country the release was issued in.',
        'category': 'ordinary',
    },
    'albumstatus': {
        'description': 'The status describes how "official" a release is. ' +
                       'Possible values are: official, promotional, ' +
                       'bootleg, pseudo-release',
        'category': 'ordinary',
    },
    'media': {
        'description': 'media',
        'category': 'ordinary',
    },
    'work': {
        'description': 'The Musicbrainzs’ work entity.',
        'category': 'ordinary',
    },
    'work_hierarchy': {
        'description': 'The hierarchy of works: The top level work appears '
                       'first. As separator is this string used: -->. '
                       'Example: Die Zauberflöte, K. 620 --> Die Zauberflöte, '
                       'K. 620: Akt I --> Die Zauberflöte, K. 620: Act I, '
                       'Scene II. No. 2 Aria "Was hör ...',
        'category': 'music_brainz',
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
    # rg?
    'rg_track_peak': {
        'description': 'rg_track_peak',
        'category': 'rg',
    },
    'r128_track_gain': {
        'description': 'An optional gain for track normalization',
        'category': 'rg',
    },
    'r128_album_gain': {
        'description': 'An optional gain for album normalization',
        'category': 'rg',
    },
    'rg_album_gain': {
        'description': 'rg_album_gain',
        'category': 'rg',
    },
    'rg_album_peak': {
        'description': 'rg_album_peak',
        'category': 'rg',
    },
    'rg_track_gain': {
        'description': 'rg_track_gain',
        'category': 'rg',
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
        'description': 'MusicBrainz releasegroup ID',
        'category': 'music_brainz',
    },
    'mb_workid': {
        'description': 'MusicBrainz work ID',
        'category': 'music_brainz',
    },
    'mb_workhierarchy_ids': {
        'description': 'All IDs in the work hierarchy. This field corresponds '
                       'to the field `work_hierarchy`. The top level work ID '
                       'appears first. As separator a slash (/) is used.'
                       'Example: e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / '
                       '5adc213f-700a-4435-9e95-831ed720f348 / '
                       'eafec51f-47c5-3c66-8c36-a524246c85f8',
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


def print_dict_sorted(dictionary, color, align='right'):
    max_field_length = get_max_field_length(dictionary)

    for key, value in sorted(dictionary.items()):
        if align == 'right':
            key = key.rjust(max_field_length, ' ')
        elif align == 'left':
            key = key.ljust(max_field_length, ' ')
        key = key + ':'
        if color:
            key = ansicolor.green(key)
            value = ansicolor.red(value)
        print(key + ' ' + value)


def print_section(text, color=False):
    if color:
        text = ansicolor.blue(text.ljust(60, ' '), reverse=True)
        line = ''
    else:
        line = '\n' + ''.ljust(60, '-')

    print('\n' + text + line)


def print_debug(media_file, MediaClass, field_generator, color=False):

    fields = MediaClass(media_file)

    # Raw mutagen values
    print_section('Raw mutagen values', color)

    mutagen_fields = {}
    for key, value in fields.mgfile.items():
        mutagen_fields[str(key)] = str(value)
    print_dict_sorted(mutagen_fields, color, align='left')

    # Class values
    print_section('Values provided by the class: ' + MediaClass.__name__,
                  color)

    class_fields = {}
    for key in field_generator():
        value = getattr(fields, key)
        if key != 'art' and value:
            value = as_string(value)
            class_fields[key] = value

    print_dict_sorted(class_fields, color, align='left')


def merge_fields(*fields):
    arguments = locals()
    out = {}
    for fields in arguments['fields']:
        out.update(fields)

    return out


def get_max_field_length(fields):
    """Get the length of the longest field in the dictionary ``fields``.

    :param dict fields: A dictionary to search for the longest field.
    """
    return max(map(len, fields))


def get_doc(additional_doc=False,
            field_prefix='$',
            field_suffix=':',
            indent=4):
    """Return a formated string containing documentation about the audio
    fields.
    """
    if additional_doc:
        f = fields.copy()
        f.update(additional_doc)
    else:
        f = fields
    field_length = get_max_field_length(f)
    field_length = field_length + len(field_prefix) + len(field_suffix) + 4
    description_indent = ' ' * (indent + field_length)
    output = ''
    for field, description in sorted(f.items()):
        description = description['description']
        field = ' ' * indent + field_prefix + field + ':'
        output += field.ljust(field_length) + \
            textwrap.fill(
                description,
                width=78,
                initial_indent=description_indent,
                subsequent_indent=description_indent
            )[field_length:] + '\n\n\n'

    return output
