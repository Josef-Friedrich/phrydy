from typing import Any, Dict, List, Literal, TypedDict

from typing_extensions import NotRequired

categories = {
    "common": "Common metadata fields",
    "music_brainz": "MusicBrainz and fingerprint information",
    "audio": "Audio information",
    "date": "Date related",
    "rg": "ReplayGain",
    "r128": "EBU R 128",
}


class FieldDoc(TypedDict):
    description: str
    category: Literal["common", "date", "audio", "music_brainz", "rg", "r128"]
    data_type: NotRequired[Literal["int", "str", "float", "list", "bool", "bytes"]]
    examples: NotRequired[List[Any]]


FieldDocCollection = Dict[str, FieldDoc]

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
    "acoustid_fingerprint": {
        "description": "Acoustic ID fingerprint",
        "category": "music_brainz",
        "data_type": "str",
    },
    "acoustid_id": {
        "description": "Acoustic ID",
        "category": "music_brainz",
        "data_type": "str",
        "examples": ["86e217b7-d3ad-4493-a9f2-cf71256ace07"],
    },
    "album": {
        "description": "album",
        "category": "common",
        "data_type": "str",
        "examples": ["Help!"],
    },
    "albumartist": {
        "description": "The artist for the entire album, which may be "
        + "different from the artists for the individual tracks",
        "category": "common",
        "data_type": "str",
        "examples": ["The Beatles"],
    },
    "albumartist_credit": {
        "description": "albumartist_credit",
        "category": "common",
        "data_type": "str",
    },
    "albumartist_sort": {
        "description": "albumartist_sort",
        "category": "common",
        "data_type": "str",
        "examples": ["Beatles, The"],
    },
    "albumartists": {
        "description": "albumartists",
        "category": "common",
        "data_type": "list",
    },
    "albumartists_credit": {
        "description": "albumartists_credit",
        "category": "common",
    },
    "albumartists_sort": {
        "description": "albumartists_sort",
        "category": "common",
    },
    # https://musicbrainz.org/doc/Disambiguation_Comment
    "albumdisambig": {
        "description": "The disambiguation album field helps to distinguish between "
        "identically named albums. The album “Weezer” for example has the "
        "disambiguation comments “Red Album” and “Green Album”.",
        "category": "common",
    },
    "albumstatus": {
        "description": 'The status describes how "official" a release is.',
        "category": "common",
        "data_type": "str",
        "examples": ["official", "promotional", "bootleg", "pseudo-release"],
    },
    "albumtype": {
        "description": "The MusicBrainz album type; the MusicBrainz wiki "
        + "has a list of type names",
        "category": "common",
        "data_type": "str",
        "examples": ["album/soundtrack"],
    },
    "albumtypes": {
        "description": "albumtypes",
        "category": "common",
    },
    "arranger": {
        "description": "A musician who creates arrangements.",
        "category": "common",
        "data_type": "str",
    },
    "art": {
        "description": "Legacy album art field.",
        "category": "common",
        "examples": [b"\xff\xd8\xff\xe0\x00"],
    },
    "artist": {
        "description": "artist",
        "category": "common",
        "data_type": "str",
        "examples": ["The Beatles"],
    },
    "artist_credit": {
        "description": "The track-specific artist credit name, which may "
        + "be a variation of the artist’s “canonical” name",
        "category": "common",
        "data_type": "str",
    },
    "artist_sort": {
        "description": "The “sort name” of the track artist.",
        "category": "common",
        "data_type": "str",
        "examples": ["Beatles, The", "White, Jack"],
    },
    "artists": {
        "description": "artists",
        "category": "common",
        "examples": [["a-ha"], ["Anouk", "Remon Stotijn"]],
    },
    "artists_credit": {
        "description": "artists_credit",
        "category": "common",
    },
    "artists_sort": {
        "description": "artists_sort",
        "category": "common",
    },
    "asin": {
        "description": "Amazon Standard Identification Number",
        "category": "common",
        "examples": ["B000002UAL"],
    },
    # barcode             : None
    # bitdepth            : 0
    # bitrate             : 80000
    # bitrate_mode        :
    # bpm                 : 6
    "barcode": {
        "description": "There are many different types of barcode, but the "
        "ones usually found on music releases are two: "
        "1. Universal Product Code (UPC), which is the "
        "original barcode used in North America. "
        "2. European Article Number (EAN)",
        "category": "common",
        "data_type": "str",
        "examples": ["5028421931838", "036000291452"],
    },
    "bitdepth": {
        "description": "only available for some formats",
        "category": "audio",
        "examples": [16],
    },
    "bitrate": {
        "description": "in kilobits per second, with units: e.g., “192kbps”",
        "category": "audio",
        "examples": [436523, 256000],
    },
    "bitrate_mode": {
        "description": "bitrate_mode",
        "category": "common",
        "examples": ["CBR"],
    },
    "bpm": {
        "description": "Beats per Minute",
        "category": "common",
    },
    # catalognum          : None
    # channels            : 1
    # comments            : the comments
    # comp                : True
    # composer            : the composer
    # composer_sort       : None
    # copyright           : None
    # country             : None
    "catalognum": {
        "description": "This is a number assigned to the release by the "
        + "label which can often be found on the spine or near "
        + "the barcode. There may be more than one, especially "
        + "when multiple labels are involved. This is not the "
        + "ASIN — there is a relationship for that — nor the "
        + "label code.",
        "category": "common",
        "examples": ["CDP 7 46439 2"],
    },
    "catalognums": {
        "description": "catalognums",
        "category": "common",
    },
    "channels": {
        "description": "channels",
        "category": "audio",
        "data_type": "int",
        "examples": [1, 2],
    },
    "comments": {
        "description": "comments",
        "category": "common",
    },
    "comp": {
        "description": "Compilation flag",
        "category": "common",
        "data_type": "bool",
        "examples": [True, False],
    },
    "composer": {
        "description": "The name of the composer.",
        "category": "common",
        "data_type": "str",
        "examples": ["Ludwig van Beethoven"],
    },
    "composer_sort": {
        "description": "The composer name for sorting.",
        "category": "common",
        "data_type": "str",
        "examples": ["Beethoven, Ludwig van"],
    },
    "copyright": {
        "description": "copyright",
        "category": "common",
    },
    "country": {
        "description": "The country the release was issued in.",
        "category": "common",
        "examples": ["NL"],
    },
    # date                : 2001-01-01
    # day                 : None
    # disc                : 4
    # disctitle           : None
    # disctotal           : 5
    "date": {
        "description": "The release data of the specific release.",
        "category": "date",
        "examples": ["1996-01-01"],
    },
    "day": {
        "description": "The release day of the specific release.",
        "category": "date",
    },
    "disc": {
        "description": "disc",
        "category": "common",
        "examples": [1],
    },
    "disctitle": {
        "description": "disctitle",
        "category": "common",
    },
    "disctotal": {
        "description": "disctotal",
        "category": "common",
        "examples": [1],
    },
    # encoder             : iTunes v7.6.2
    # encoder_info        :
    # encoder_settings    :
    "encoder": {
        # https://id3.org/id3v2.4.0-frames
        "description": "the name of the person or organisation that encoded the audio "
        "file. This field may contain a copyright message, if the audio "
        "file also is copyrighted by the encoder.",
        "category": "common",
        "examples": ["iTunes v7.6.2"],
    },
    "encoder_info": {
        "description": "encoder_info",
        "category": "common",
        "examples": ["LAME 3.92.0+"],
    },
    "encoder_settings": {
        "description": "encoder_settings",
        "category": "common",
        "examples": ["-b 255+"],
    },
    # format              : MP3
    "format": {
        "description": "e.g., “MP3” or “FLAC”",
        "category": "audio",
        "examples": ["MP3", "FLAC"],
    },
    # genre               : the genre
    # genres              : ['the genre']
    # grouping            : the grouping
    "genre": {"description": "genre", "category": "common", "examples": ["Rock"]},
    "genres": {"description": "genres", "category": "common", "examples": [["Rock"]]},
    "grouping": {
        # https://docs.microsoft.com/en-us/windows/win32/wmp/wm-contentgroupdescription-attribute
        "description": "A content group, which is a collection of media items "
        "such as a CD boxed set.",
        "category": "common",
    },
    # images              : []
    # initial_key         : None
    # isrc                : None
    "images": {
        "description": "images",
        "category": "common",
        "examples": [["<mediafile.Image object at 0x7f51fce26b20>"]],
    },
    "initial_key": {
        # https://id3.org/id3v2.4.0-frames
        "description": "The Initial key frame contains the musical key in "
        "which the sound starts. It is represented as a "
        "string with a maximum length of three characters. "
        'The ground keys are represented with "A","B","C",'
        '"D","E", "F" and "G" and halfkeys represented with '
        '"b" and "#". Minor is represented as "m".',
        "category": "common",
        "examples": ["Dbm"],
    },
    "isrc": {
        "description": "The International Standard Recording Code, "
        "abbreviated to ISRC, is a system of codes that "
        "identify audio and music video recordings.",
        "category": "common",
        "examples": ["CAC118989003", "ITO101117740"],
    },
    # label               : the label
    # language            : None
    # length              : 1.071
    # lyricist            : None
    # lyrics              : the lyrics
    "label": {
        "description": "The label which issued the release. There may be "
        + "more than one.",
        "category": "common",
        "examples": ["Brilliant Classics", "wea"],
    },
    "language": {
        "description": "The language a release’s track list is written in. "
        + "The possible values are taken from the ISO 639-3 "
        + "standard.",
        "category": "common",
        "examples": ["zxx", "eng"],
    },
    "languages": {
        "description": "languages",
        "category": "common",
    },
    "length": {
        "description": "The length of a recording in seconds.",
        "category": "audio",
        "examples": [674.4666666666667],
    },
    "lyricist": {
        # https://id3.org/id3v2.4.0-frames
        "description": "The writer of the text or lyrics in the recording.",
        "data_type": "str",
        "category": "common",
    },
    "lyrics": {
        # https://id3.org/id3v2.4.0-frames
        "description": "The lyrics of the song or a text transcription of "
        "other vocal activities.",
        "data_type": "str",
        "category": "common",
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
    "mb_albumartistid": {
        "description": "MusicBrainz album artist ID.",
        "category": "music_brainz",
        "data_type": "str",
        "examples": [
            "1f9df192-a621-4f54-8850-2c5373b7eac9",
            "b972f589-fb0e-474e-b64a-803b0364fa75",
        ],
    },
    "mb_albumartistids": {
        "description": "MusicBrainz album artist IDs as a list.",
        "category": "music_brainz",
        "examples": [
            [
                "b972f589-fb0e-474e-b64a-803b0364fa75",
                "dea28aa9-1086-4ffa-8739-0ccc759de1ce",
                "d2ced2f1-6b58-47cf-ae87-5943e2ab6d99",
            ]
        ],
        "data_type": "list",
    },
    "mb_albumid": {
        "description": "MusicBrainz album ID.",
        "category": "music_brainz",
        "examples": ["fd6adc77-1489-4a13-9aa0-32951061d92b"],
        "data_type": "str",
    },
    "mb_artistid": {
        "description": "MusicBrainz artist ID.",
        "category": "music_brainz",
        "examples": ["1f9df192-a621-4f54-8850-2c5373b7eac9"],
        "data_type": "str",
    },
    "mb_artistids": {
        "description": "MusicBrainz artist IDs as a list.",
        "category": "music_brainz",
        "examples": [["1f9df192-a621-4f54-8850-2c5373b7eac9"]],
        "data_type": "list",
    },
    "mb_releasegroupid": {
        "description": "MusicBrainz releasegroup ID.",
        "category": "music_brainz",
        "examples": ["f714fd70-aaca-4863-9d0d-2768a53acaeb"],
        "data_type": "str",
    },
    "mb_releasetrackid": {
        "description": "MusicBrainz release track ID.",
        "category": "music_brainz",
        "examples": ["38c8c114-5e3b-484f-8af0-79c47ef9c169"],
        "data_type": "str",
    },
    "mb_trackid": {
        "description": "MusicBrainz track ID.",
        "category": "music_brainz",
        "examples": ["c390b132-4a44-4e16-bec3-bffbbcaa19aa"],
        "data_type": "str",
    },
    "mb_workid": {
        "description": "MusicBrainz work ID.",
        "category": "music_brainz",
        "examples": ["508ec4b1-9549-38cd-a61e-1f0d120a6118"],
        "data_type": "str",
    },
    "mb_workhierarchy_ids": {
        "description": "All IDs in the work hierarchy. This field corresponds "
        "to the field `work_hierarchy`. The top level work ID "
        "appears first. A slash (/) is used as separator.",
        "category": "music_brainz",
        "examples": [
            "e208c5f5-5d37-3dfc-ac0b-999f207c9e46 / "
            "5adc213f-700a-4435-9e95-831ed720f348 / "
            "eafec51f-47c5-3c66-8c36-a524246c85f8"
        ],
        "data_type": "str",
    },
    "media": {
        "description": "A prototypical medium is one of the physical, separate things "
        "you would get when you buy something in a record store.",
        "category": "common",
        "examples": ["CD"],
        "data_type": "str",
    },
    "month": {
        "description": "The release month of the specific release.",
        "category": "date",
        "examples": [11],
        "data_type": "int",
    },
    # original_date       : None
    # original_day        : None
    # original_month      : None
    # original_year       : None
    "original_date": {
        "description": "The release date of the original version of the " "album.",
        "category": "date",
        "examples": ["1991-11-04"],
        "data_type": "str",
    },
    "original_day": {
        "description": "The release day of the original version of the album.",
        "category": "date",
        "examples": [4],
        "data_type": "int",
    },
    "original_month": {
        "description": "The release month of the original version of the " + "album.",
        "category": "date",
        "examples": [11],
        "data_type": "int",
    },
    "original_year": {
        "description": "The release year of the original version of the " "album.",
        "category": "date",
        "examples": [1991],
        "data_type": "int",
    },
    # r128_album_gain     : None
    # r128_track_gain     : None
    # releasegroup_types  : None
    # rg_album_gain       : None
    # rg_album_peak       : None
    # rg_track_gain       : 0.0
    # rg_track_peak       : 0.000244
    "r128_album_gain": {
        # https://en.wikipedia.org/wiki/EBU_R_128
        "description": "An optional gain for album normalization. EBU R 128 is a "
        "recommendation for loudness normalisation and maximum level of "
        "audio signals.",
        "category": "r128",
    },
    "r128_track_gain": {
        # https://en.wikipedia.org/wiki/EBU_R_128
        "description": "An optional gain for track normalization. EBU R 128 is a "
        "recommendation for loudness normalisation and maximum level of "
        "audio signals.",
        "category": "r128",
    },
    "releasegroup_types": {
        "description": "This field collects all items in the MusicBrainz’ API "
        " related to type: `type`, `primary-type and "
        "`secondary-type-list`. Main usage of this field is to "
        "determine in a secure manner if the release is a "
        "soundtrack.",
        "category": "music_brainz",
    },
    "rg_album_gain": {
        "description": "ReplayGain Album Gain, "
        "see https://en.wikipedia.org/wiki/ReplayGain.",
        "category": "rg",
    },
    "rg_album_peak": {
        "description": "ReplayGain Album Peak, "
        "see https://en.wikipedia.org/wiki/ReplayGain.",
        "category": "rg",
    },
    "rg_track_gain": {
        "description": "ReplayGain Track Gain, "
        "see https://en.wikipedia.org/wiki/ReplayGain.",
        "category": "rg",
        "examples": [0.0],
    },
    "rg_track_peak": {
        "description": "ReplayGain Track Peak, "
        "see https://en.wikipedia.org/wiki/ReplayGain.",
        "category": "rg",
        "examples": [0.000244],
    },
    # samplerate          : 44100
    # script              : None
    "samplerate": {
        "description": "The sample rate as an integer number.",
        "category": "audio",
        "examples": [44100],
        "data_type": "int",
    },
    "script": {
        "description": "The script used to write the release’s track list. "
        + "The possible values are taken from the ISO 15924 "
        + "standard.",
        "category": "common",
        "examples": ["Latn"],
        "data_type": "str",
    },
    # title               : full
    # track               : 2
    # tracktotal          : 3
    "title": {
        "description": "The title of a audio file.",
        "category": "common",
        "examples": [
            "32 Variations for Piano in C minor on an Original " "Theme, WoO 80"
        ],
        "data_type": "str",
    },
    "track": {
        "description": "The track number.",
        "category": "common",
        "data_type": "int",
        "examples": [1],
    },
    "tracktotal": {
        "description": "The total track number.",
        "category": "common",
        "data_type": "int",
        "examples": [12],
    },
    # url                 : None
    "url": {
        "description": "Uniform Resource Locator.",
        "category": "common",
        "data_type": "str",
    },
    # work                : None
    # work_hierarchy      : None
    "work": {
        "description": "The Musicbrainzs’ work entity.",
        "category": "common",
        "examples": [
            "32 Variations for Piano in C minor on an Original " "Theme, WoO 80"
        ],
        "data_type": "str",
    },
    "work_hierarchy": {
        "description": "The hierarchy of works: The top level work appears "
        "first. As separator is this string used: -->.",
        "category": "music_brainz",
        "examples": [
            "Die Zauberflöte, K. 620 --> Die Zauberflöte, "
            "K. 620: Akt I --> Die Zauberflöte, K. 620: Act I, "
            'Scene II. No. 2 Aria "Was hör ...'
        ],
        "data_type": "str",
    },
    # year                : 2001
    "year": {
        "description": "The release year of the specific release.",
        "category": "date",
        "examples": [2001],
        "data_type": "int",
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
