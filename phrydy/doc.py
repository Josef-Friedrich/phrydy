import textwrap
import ansicolor
import typing
from typing import Union, Literal, List, Any
from typing_extensions import NotRequired

from phrydy.mediafile_extended import MediaFileExtended


class FieldDoc(typing.TypedDict):
    description: str
    # ordinary: Ordinary metadata
    # music_brainz: MusicBrainz and fingerprint information
    # audio: Audio information
    # date: Date related
    category: Literal['ordinary', 'date', 'audio', 'music_brainz', 'rg']
    data_type: NotRequired[Literal['int', 'str', 'float', 'list', 'bool']]
    examples: NotRequired[Union[Any, List[Any]]]


FieldDocCollection = typing.Dict[str, FieldDoc]

fields: FieldDocCollection = {
    # acoustid_fingerprint: None
    # acoustid_id         : None
    # album               : the album
    # albumartist         : the album artist
    # albumartist_credit  : None
    # albumartist_sort    : None
    # albumartists        : []
    # albumdisambig       : None
    # albumstatus         : None
    # albumtype           : None
    # arranger            : None
    # art                 : None
    # artist              : the artist
    # artist_credit       : None
    # artist_sort         : None
    # artists             : []
    # asin                : None
    'acoustid_fingerprint': {
        'description': 'Acoustic ID fingerprint',
        'category': 'music_brainz',
        'data_type': 'str',
    },
    'acoustid_id': {
        'description': 'Acoustic ID',
        'category': 'music_brainz',
        'data_type': 'str',
    },
    'album': {
        'description': 'album',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'albumartist': {
        'description': 'The artist for the entire album, which may be ' +
                       'different from the artists for the individual tracks',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'albumartist_credit': {
        'description': 'albumartist_credit',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'albumartist_sort': {
        'description': 'albumartist_sort',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'albumartists': {
        'description': 'albumartists',
        'category': 'ordinary',
        'data_type': 'list',
    },
    'albumdisambig': {
        'description': 'albumdisambig',
        'category': 'ordinary',
    },
    'albumstatus': {
        'description': 'The status describes how "official" a release is. ' +
                       'Possible values are: official, promotional, ' +
                       'bootleg, pseudo-release',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'albumtype': {
        'description': 'The MusicBrainz album type; the MusicBrainz wiki ' +
                       'has a list of type names',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'arranger': {
        'description': 'arranger',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'art': {
        'description': 'art',
        'category': 'ordinary',
    },
    'artist': {
        'description': 'artist',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'artist_credit': {
        'description': 'The track-specific artist credit name, which may ' +
                       'be a variation of the artist’s “canonical” name',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'artist_sort': {
        'description': 'The “sort name” of the track artist (e.g., ' +
                       '“Beatles, The” or “White, Jack”)',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'artists': {
        'description': 'artists',
        'category': 'ordinary',
    },
    'asin': {
        'description': 'Amazon Standard Identification Number',
        'category': 'ordinary',
    },
    # barcode             : None
    # bitdepth            : 0
    # bitrate             : 80000
    # bitrate_mode        :
    # bpm                 : 6
    'barcode': {
        'description': 'barcode',
        'category': 'ordinary',
    },
    'bitdepth': {
        'description': 'only available for some formats',
        'category': 'audio',
    },
    'bitrate': {
        'description': 'in kilobits per second, with units: e.g., “192kbps”',
        'category': 'audio',
    },
    'bitrate_mode': {
        'description': 'bitrate_mode',
        'category': 'ordinary',
    },
    'bpm': {
        'description': 'Beats per Minute',
        'category': 'ordinary',
    },
    # catalognum          : None
    # channels            : 1
    # comments            : the comments
    # comp                : True
    # composer            : the composer
    # composer_sort       : None
    # copyright           : None
    # country             : None
    'catalognum': {
        'description': 'This is a number assigned to the release by the ' +
                       'label which can often be found on the spine or near ' +
                       'the barcode. There may be more than one, especially ' +
                       'when multiple labels are involved. This is not the ' +
                       'ASIN — there is a relationship for that — nor the ' +
                       'label code.',
        'category': 'ordinary',
    },
    'channels': {
        'description': 'channels',
        'category': 'audio',
        'data_type': 'int',
        'examples': 1,
    },
    'comments': {
        'description': 'comments',
        'category': 'ordinary',
    },
    'comp': {
        'description': 'Compilation flag',
        'category': 'ordinary',
        'data_type': 'bool',
        'examples': [True, False],
    },
    'composer': {
        'description': 'composer',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'composer_sort': {
        'description': 'Composer name for sorting.',
        'category': 'ordinary',
        'data_type': 'str',
    },
    'copyright': {
        'description': 'copyright',
        'category': 'ordinary',
    },
    'country': {
        'description': 'The country the release was issued in.',
        'category': 'ordinary',
    },
    # date                : 2001-01-01
    # day                 : None
    # disc                : 4
    # disctitle           : None
    # disctotal           : 5
    'date': {
        'description': 'date',
        'category': 'date',
    },
    'day': {
        'description': 'The release day of the specific release',
        'category': 'date',
    },
    'disc': {
        'description': 'disc',
        'category': 'ordinary',
    },
    'disctitle': {
        'description': 'disctitle',
        'category': 'ordinary',
    },
    'disctotal': {
        'description': 'disctotal',
        'category': 'ordinary',
    },
    # encoder             : iTunes v7.6.2
    # encoder_info        :
    # encoder_settings    :
    'encoder': {
        'description': 'encoder',
        'category': 'ordinary',
        'examples': 'iTunes v7.6.2',
    },
    'encoder_info': {
        'description': 'encoder_info',
        'category': 'ordinary',
    },
    'encoder_settings': {
        'description': 'encoder_settings',
        'category': 'ordinary',
    },
    # format              : MP3
    'format': {
        'description': 'e.g., “MP3” or “FLAC”',
        'category': 'audio',
        'examples': ['MP3', 'FLAC']
    },
    # genre               : the genre
    # genres              : ['the genre']
    # grouping            : the grouping
    'genre': {
        'description': 'genre',
        'category': 'ordinary',
    },
    'genres': {
        'description': 'genres',
        'category': 'ordinary',
    },
    'grouping': {
        'description': 'grouping',
        'category': 'ordinary',
    },
    # images              : []
    # initial_key         : None
    # isrc                : None
    'images': {
        'description': 'images',
        'category': 'ordinary',
    },
    'initial_key': {
        'description': 'initial_key',
        'category': 'ordinary',
    },
    'isrc': {
        'description': 'isrc',
        'category': 'ordinary',
    },
    # label               : the label
    # language            : None
    # length              : 1.071
    # lyricist            : None
    # lyrics              : the lyrics
    'label': {
        'description': 'The label which issued the release. There may be ' +
                       'more than one.',
        'category': 'ordinary',
    },
    'language': {
        'description': 'The language a release’s track list is written in. ' +
                       'The possible values are taken from the ISO 639-3 ' +
                       'standard.',
        'category': 'ordinary',
    },
    'length': {
        'description': 'in seconds',
        'category': 'audio',
    },
    'lyricist': {
        'description': 'lyricist',
        'category': 'ordinary',
    },
    'lyrics': {
        'description': 'lyrics',
        'category': 'ordinary',
    },
    # media               : None
    # month               : None
    # mb_albumartistid    : None
    # mb_albumartistids   : []
    # mb_albumid          : 9e873859-8aa4-4790-b985-5a953e8ef628
    # mb_artistid         : 7cf0ea9d-86b9-4dad-ba9e-2355a64899ea
    # mb_artistids        : ['7cf0ea9d-86b9-4dad-ba9e-2355a64899ea']
    # mb_releasegroupid   : None
    # mb_releasetrackid   : c29f3a57-b439-46fd-a2e2-93776b1371e0
    # mb_trackid          : 8b882575-08a5-4452-a7a7-cbb8a1531f9e
    # mb_workhierarchy_ids: None
    # mb_workid           : None
    'mb_trackid': {
        'description': 'MusicBrainz track ID',
        'category': 'music_brainz',
    },
    'mb_releasetrackid': {
        'description': 'MusicBrainz release track ID',
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
    'mb_artistids': {
        'description': 'mb_artistids',
        'category': 'music_brainz',
    },
    'mb_albumartistid': {
        'description': 'MusicBrainz album artist ID',
        'category': 'music_brainz',
        'examples': 'b972f589-fb0e-474e-b64a-803b0364fa75',
        'data_type': 'str',
    },
    'mb_albumartistids': {
        'description': 'mb_albumartistids',
        'category': 'music_brainz',
        'examples': [
            ['b972f589-fb0e-474e-b64a-803b0364fa75',
             'dea28aa9-1086-4ffa-8739-0ccc759de1ce',
             'd2ced2f1-6b58-47cf-ae87-5943e2ab6d99']
        ],
        'data_type': 'list',
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
                       'appears first. A slash (/) is used as separator.'
                       'Example: e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / '
                       '5adc213f-700a-4435-9e95-831ed720f348 / '
                       'eafec51f-47c5-3c66-8c36-a524246c85f8',
        'category': 'music_brainz',
    },
    'media': {
        'description': 'media',
        'category': 'ordinary',
    },
    'month': {
        'description': 'The release month of the specific release',
        'category': 'date',
    },
    # original_date       : None
    # original_day        : None
    # original_month      : None
    # original_year       : None
    'original_date': {
        'description': 'original_date',
        'category': 'date',
    },
    'original_day': {
        'description': 'The release day of the original version of the album',
        'category': 'date',
    },
    'original_month': {
        'description': 'The release month of the original version of the ' +
                       'album',
        'category': 'date',
    },
    'original_year': {
        'description': 'The release year of the original version of the album',
        'category': 'date',
    },
    # r128_album_gain     : None
    # r128_track_gain     : None
    # releasegroup_types  : None
    # rg_album_gain       : None
    # rg_album_peak       : None
    # rg_track_gain       : 0.0
    # rg_track_peak       : 0.000244
    'r128_album_gain': {
        'description': 'An optional gain for album normalization',
        'category': 'rg',
    },
    'r128_track_gain': {
        'description': 'An optional gain for track normalization',
        'category': 'rg',
    },
    'releasegroup_types': {
        'description': 'This field collects all items in the MusicBrainz’ API '
                       ' related to type: `type`, `primary-type and '
                       '`secondary-type-list`. Main usage of this field is to '
                       'determine in a secure manner if the release is a '
                       'soundtrack.',
        'category': 'music_brainz',
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
        'examples': 0.0,
    },
    'rg_track_peak': {
        'description': 'rg_track_peak',
        'category': 'rg',
        'examples': 0.000244,
    },
    # samplerate          : 44100
    # script              : None
    'samplerate': {
        'description': 'in kilohertz, with units: e.g., “48kHz”',
        'category': 'audio',
    },
    'script': {
        'description': 'The script used to write the release’s track list. ' +
                       'The possible values are taken from the ISO 15924 ' +
                       'standard.',
        'category': 'ordinary',
    },
    # title               : full
    # track               : 2
    # tracktotal          : 3
    'title': {
        'description': 'The title of a audio file.',
        'category': 'ordinary',
    },
    'track': {
        'description': 'track',
        'category': 'ordinary',
        'examples': 1,
    },
    'tracktotal': {
        'description': 'tracktotal',
        'category': 'ordinary',
        'examples': 12,
    },
    # url                 : None
    'url': {
        'description': 'Uniform Resource Locator.',
        'category': 'ordinary',
    },
    # work                : None
    # work_hierarchy      : None
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
    # year                : 2001
    'year': {
        'description': 'The release year of the specific release',
        'category': 'date',
        'examples': 2001,
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


def get_type_name(t: typing.Any) -> str:
    return type(t).__name__


def print_dict_sorted(dictionary: typing.Dict[str, typing.Any],
                      color: bool,
                      align: typing.Literal['left', 'right'] = 'right'
                      ) -> None:
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


def print_section(text: str, color: bool = False) -> None:
    if color:
        text = ansicolor.blue(text.ljust(60, ' '), reverse=True)
        line = ''
    else:
        line = '\n' + ''.ljust(60, '-')

    print('\n' + text + line)


def print_debug(media_file: str,
                MediaClass: typing.Callable[[str], MediaFileExtended],
                field_generator: typing.Callable[
                    [], typing.Generator[str, None, None]
                ],
                color: bool = False) -> None:
    fields = MediaClass(media_file)

    # All class values
    print_section('All values provided by the class: ' + MediaClass.__name__,
                  color)

    class_fields = {}
    for key in field_generator():
        value = getattr(fields, key)
        class_fields[key] = str(value)

    print_dict_sorted(class_fields, color, align='left')

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
            class_fields[key] = str(value)

    print_dict_sorted(class_fields, color, align='left')


def merge_fields(*fields):
    """Used in audiorename/args.py"""
    arguments = locals()
    out = {}
    for fields in arguments['fields']:
        out.update(fields)

    return out


def get_max_field_length(fields) -> int:
    """Get the length of the longest field in the dictionary ``fields``.

    :param dict fields: A dictionary to search for the longest field.
    """
    return max(map(len, fields))


def get_doc(additional_doc: typing.Optional[FieldDocCollection] = None,
            field_prefix: str = '$',
            field_suffix: str = ':',
            indent: int = 4):
    """Return a formated string containing the documentation about the audio
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
