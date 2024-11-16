import datetime
import enum
from collections.abc import Generator, Sequence
from io import BufferedRandom, BufferedReader
from pathlib import Path
from typing import Any, Literal, Optional, Union

from _typeshed import Incomplete
from mutagen import FileType as MutagenFile

__all__ = ["UnreadableFileError", "FileTypeError", "MediaFile"]

class UnreadableFileError(Exception):
    def __init__(self, filename, msg) -> None: ...

class FileTypeError(UnreadableFileError):
    def __init__(self, filename, mutagen_type: Incomplete | None = None) -> None: ...

class MutagenError(UnreadableFileError):
    def __init__(self, filename, mutagen_exc) -> None: ...

class ImageType(enum.Enum):
    other = 0
    icon = 1
    other_icon = 2
    front = 3
    back = 4
    leaflet = 5
    media = 6
    lead_artist = 7
    artist = 8
    conductor = 9
    group = 10
    composer = 11
    lyricist = 12
    recording_location = 13
    recording_session = 14
    performance = 15
    screen_capture = 16
    fish = 17
    illustration = 18
    artist_logo = 19
    publisher_logo = 20

class Image:
    data: Incomplete
    desc: Incomplete
    type: Incomplete
    def __init__(
        self, data, desc: Incomplete | None = None, type: Incomplete | None = None
    ) -> None: ...
    @property
    def mime_type(self): ...
    @property
    def type_index(self): ...

AsType = Union[type[bool], type[int], type[str], type[float]]

MutagenValue = Optional[Union[str, bytes]]
MutagenValues = Sequence[MutagenValue]

class StorageStyle:
    formats: Incomplete
    key: str
    as_type: AsType
    suffix: Optional[str]
    float_places: int
    read_only: bool
    def __init__(
        self,
        key: str,
        as_type: AsType = ...,
        suffix: str | None = None,
        float_places: int = 2,
        read_only: bool = False,
    ) -> None: ...
    def get(self, mutagen_file: MutagenFile): ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def deserialize(self, mutagen_value: MutagenValue): ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def store(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def serialize(self, value: MutagenValue): ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class ListStorageStyle(StorageStyle):
    def get(self, mutagen_file: MutagenFile): ...
    def get_list(self, mutagen_file: MutagenFile): ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def set_list(self, mutagen_file: MutagenFile, values: MutagenValues) -> None: ...
    def store(self, mutagen_file: MutagenFile, values: MutagenValues) -> None: ...

class SoundCheckStorageStyleMixin:
    def get(self, mutagen_file: MutagenFile): ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...

class ASFStorageStyle(ListStorageStyle):
    formats: Incomplete
    def deserialize(self, data): ...

class MP4StorageStyle(StorageStyle):
    formats: Incomplete
    def serialize(self, value): ...

class MP4TupleStorageStyle(MP4StorageStyle):
    index: Incomplete
    def __init__(self, key: str, index: int = 0, **kwargs) -> None: ...
    def deserialize(self, mutagen_value: MutagenValues): ...
    def get(self, mutagen_file: MutagenFile): ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class MP4ListStorageStyle(ListStorageStyle, MP4StorageStyle): ...

class MP4SoundCheckStorageStyle(SoundCheckStorageStyleMixin, MP4StorageStyle):
    index: Incomplete
    def __init__(self, key: str, index: int = 0, **kwargs) -> None: ...

class MP4BoolStorageStyle(MP4StorageStyle):
    def get(self, mutagen_file: MutagenFile): ...
    def get_list(self, mutagen_file: MutagenFile) -> None: ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def set_list(self, mutagen_file: MutagenFile, values: MutagenValue) -> None: ...

class MP4ImageStorageStyle(MP4ListStorageStyle):
    def __init__(self, **kwargs) -> None: ...
    def deserialize(self, data): ...
    def serialize(self, image): ...

class MP3StorageStyle(StorageStyle):
    formats: Incomplete
    id3_lang: Incomplete
    def __init__(
        self, key: str, id3_lang: Incomplete | None = None, **kwargs
    ) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...

class MP3PeopleStorageStyle(MP3StorageStyle):
    involvement: Incomplete
    def __init__(self, key: str, involvement: str = "", **kwargs) -> None: ...
    def store(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...

class MP3ListStorageStyle(ListStorageStyle, MP3StorageStyle):
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, values: MutagenValues) -> None: ...

class MP3UFIDStorageStyle(MP3StorageStyle):
    owner: Incomplete
    def __init__(self, owner, **kwargs) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...

class MP3DescStorageStyle(MP3StorageStyle):
    description: Incomplete
    attr: Incomplete
    multispec: Incomplete
    def __init__(
        self,
        desc: str = "",
        key: str = "TXXX",
        attr: str = "text",
        multispec: bool = True,
        **kwargs,
    ) -> None: ...
    def store(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class MP3ListDescStorageStyle(MP3DescStorageStyle, ListStorageStyle):
    split_v23: Incomplete
    def __init__(
        self, desc: str = "", key: str = "TXXX", split_v23: bool = False, **kwargs
    ) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, values: MutagenValues) -> None: ...

class MP3SlashPackStorageStyle(MP3StorageStyle):
    pack_pos: Incomplete
    def __init__(self, key: str, pack_pos: int = 0, **kwargs) -> None: ...
    def get(self, mutagen_file: MutagenFile): ...
    def set(self, mutagen_file: MutagenFile, value: MutagenValue) -> None: ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class MP3ImageStorageStyle(ListStorageStyle, MP3StorageStyle):
    as_type: Incomplete
    def __init__(self) -> None: ...
    def deserialize(self, apic_frame): ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, frames) -> None: ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...
    def serialize(self, image): ...

class MP3SoundCheckStorageStyle(SoundCheckStorageStyleMixin, MP3DescStorageStyle):
    index: Incomplete
    def __init__(self, index: int = 0, **kwargs) -> None: ...

class ASFImageStorageStyle(ListStorageStyle):
    formats: Incomplete
    def __init__(self) -> None: ...
    def deserialize(self, asf_picture): ...
    def serialize(self, image): ...

class VorbisImageStorageStyle(ListStorageStyle):
    formats: Incomplete
    as_type: Incomplete
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def store(self, mutagen_file: MutagenFile, image_data) -> None: ...
    def serialize(self, image): ...

class FlacImageStorageStyle(ListStorageStyle):
    formats: Incomplete
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def deserialize(self, flac_picture): ...
    def store(self, mutagen_file: MutagenFile, pictures) -> None: ...
    def serialize(self, image): ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class APEv2ImageStorageStyle(ListStorageStyle):
    formats: Incomplete
    TAG_NAMES: Incomplete
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file: MutagenFile): ...
    def set_list(self, mutagen_file: MutagenFile, values: MutagenValues) -> None: ...
    def delete(self, mutagen_file: MutagenFile) -> None: ...

class MediaField:
    out_type: Incomplete
    def __init__(self, *styles, **kwargs) -> None: ...
    def styles(self, mutagen_file: MutagenFile) -> Generator[Incomplete]: ...
    def __get__(self, mediafile: MediaFile, owner: Incomplete | None = None): ...
    def __set__(self, mediafile: MediaFile, value: MutagenValue) -> None: ...
    def __delete__(self, mediafile: MediaFile) -> None: ...

class ListMediaField(MediaField):
    def __get__(self, mediafile: MediaFile, _: Incomplete | None = None): ...
    def __set__(self, mediafile: MediaFile, values: MutagenValues) -> None: ...
    def single_field(self): ...

class DateField(MediaField):
    def __init__(self, *date_styles, **kwargs) -> None: ...
    def __get__(self, mediafile: MediaFile, owner: Incomplete | None = None): ...
    def __set__(self, mediafile: MediaFile, date) -> None: ...
    def __delete__(self, mediafile: MediaFile) -> None: ...
    def year_field(self) -> DateItemField: ...
    def month_field(self) -> DateItemField: ...
    def day_field(self) -> DateItemField: ...

class DateItemField(MediaField):
    date_field: Incomplete
    item_pos: Incomplete
    def __init__(self, date_field, item_pos) -> None: ...
    def __get__(self, mediafile: MediaFile, _): ...
    def __set__(self, mediafile: MediaFile, value: MutagenValue) -> None: ...
    def __delete__(self, mediafile: MediaFile) -> None: ...

class CoverArtField(MediaField):
    def __init__(self) -> None: ...
    def __get__(self, mediafile: MediaFile, _): ...
    @staticmethod
    def guess_cover_image(candidates): ...
    def __set__(self, mediafile: MediaFile, data) -> None: ...
    def __delete__(self, mediafile: MediaFile) -> None: ...

class QNumberField(MediaField):
    def __init__(self, fraction_bits, *args, **kwargs) -> None: ...
    def __get__(self, mediafile: MediaFile, owner: Incomplete | None = None): ...
    def __set__(self, mediafile: MediaFile, value: MutagenValue) -> None: ...

class ImageListField(ListMediaField):
    def __init__(self) -> None: ...

FileThing = Union[
    str,
    Path,
    BufferedReader,  # open(..., 'rb')
    BufferedRandom,  # open(..., 'rb+')
]

class MediaFile:
    def __init__(self, filething: FileThing, id3v23: bool = False) -> None:
        """Constructs a new `MediaFile` reflecting the provided file.

        `filething` can be a path to a file (i.e., a string) or a
        file-like object.

        May throw `UnreadableFileError`.

        By default, MP3 files are saved with ID3v2.4 tags. You can use
        the older ID3v2.3 standard by specifying the `id3v23` option.
        """
        ...
    __name__: str

    mgfile: MutagenFile

    @property
    def filename(self) -> str:  # type: ignore
        """The name of the file.

        This is the path if this object was opened from the filesystem,
        or the name of the file-like object.
        """
        ...

    @property
    def path(self) -> Optional[str]:  # type: ignore
        """The path to the file.

        This is `None` if the data comes from a file-like object instead
        of a filesystem path.
        """
        ...

    @property
    def filesize(self) -> int:  # type: ignore
        """The size (in bytes) of the underlying file."""
        ...

    def save(self, **kwargs: Any) -> None:
        """Write the object's tags back to the file.

        May throw `UnreadableFileError`. Accepts keyword arguments to be
        passed to Mutagen's `save` function.
        """
        ...

    def delete(self) -> None:
        """Remove the current metadata tag from the file. May
        throw `UnreadableFileError`.
        """
        ...

    @classmethod
    def fields(cls) -> Generator[str, Any, None]:  # type: ignore
        """Get the names of all writable properties that reflect
        metadata tags (i.e., those that are instances of
        :class:`MediaField`).
        """
        ...

    @classmethod
    def sorted_fields(cls) -> Generator[str, Any, None]:  # type: ignore
        """Get the names of all writable metadata fields, sorted in the
        order that they should be written.

        This is a lexicographic order, except for instances of
        :class:`DateItemField`, which are sorted in year-month-day
        order.
        """
        ...

    @classmethod
    def readable_fields(cls) -> Generator[str, Any, None]:  # type: ignore
        """Get all metadata fields: the writable ones from
        :meth:`fields` and also other audio properties.
        """
        ...

    @classmethod
    def add_field(cls, name: str, descriptor: MediaField) -> None:
        """Add a field to store custom tags.

        :param name: the name of the property the field is accessed
                     through. It must not already exist on this class.

        :param descriptor: an instance of :class:`MediaField`.
        """
        ...

    def update(self, dict: dict[str, Any]) -> None:
        """Set all field values from a dictionary.

        For any key in `dict` that is also a field to store tags the
        method retrieves the corresponding value from `dict` and updates
        the `MediaFile`. If a key has the value `None`, the
        corresponding property is deleted from the `MediaFile`.
        """
        ...

    def as_dict(self) -> dict[str, Any]:  # type: ignore
        """Get a dictionary with all writable properties that reflect
        metadata tags (i.e., those that are instances of
        :class:`MediaField`).
        """
        ...

    # Field definitions.

    title: Optional[str]
    """
    The title of the track.
    """

    artist: Optional[str]
    """"The track artist names, separated by the specified join phrases."""

    artists: Optional[list[str]]
    """A multi-value field containing the track artist names."""

    album: Optional[str]
    """The title of the release."""

    genres: Optional[list[str]]
    """Genres are currently supported in MusicBrainz as part of the tag system."""

    genre: Optional[str]
    """Genres are currently supported in MusicBrainz as part of the tag system."""

    lyricist: Optional[str]
    """The writer of the text or lyrics in the recording."""

    composer: Optional[str]
    """The name of the composer."""

    composer_sort: Optional[str]
    """The composer name for sorting."""

    arranger: Optional[str]
    """A musician who creates arrangements."""

    grouping: Optional[str]
    """A content group, which is a collection of media items such as a CD boxed set."""

    track: Optional[int]
    """The number of the track on the disc."""

    tracktotal: Optional[int]
    """The total number of tracks on this disc."""

    disc: Optional[int]
    """The number of the disc."""

    disctotal: Optional[int]
    """The total number of discs."""

    url: Optional[str]
    """Uniform Resource Locator."""

    lyrics: Optional[str]
    """The lyrics of the song or a text transcription of other vocal activities."""

    comments: Optional[str]
    """The disambiguation comment entered to help distinguish one release from another (e.g.: Deluxe version with 2 bonus tracks)."""

    copyright: Optional[str]
    """The copyright message for the copyright holder of the original sound, beginning with a year and a space character."""

    bpm: Optional[int]
    """"The number of beats per minute of the track."""

    comp: Optional[bool]
    """Compilation flag."""

    albumartist: Optional[str]
    """The artist for the entire album, which may be different from the artists for the individual tracks. The artists primarily credited on the release, separated by the specified join phrases."""

    albumartists: Optional[list[str]]
    """The album artists specifed as a list."""

    albumtypes: Optional[list[str]]
    """"The MusicBrainz release group types; the MusicBrainz wiki has a list of type names."""

    albumtype: Optional[str]
    """"The primary MusicBrainz release group type; the MusicBrainz wiki has a list of type names."""

    label: Optional[str]
    """The label which issued the release. There may be more than one."""

    artist_sort: Optional[str]
    """The “sort name” of the track artist."""

    albumartist_sort: Optional[str]
    """The “sort name” of the artist for the entire album."""

    asin: Optional[str]
    """The Amazon Standard Identification Number - the number identifying the item on Amazon."""

    catalognums: Optional[list[str]]
    """Multiple numbers assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved."""

    catalognum: Optional[str]
    """A number assigned to the release by the label which can often be found on the spine or near the barcode. There may be more than one, especially when multiple labels are involved."""

    barcode: Optional[str]
    """The barcode assigned to the release. There are many different types of barcode, but the ones usually found on music releases are two: 1. Universal Product Code (UPC), which is the original barcode used in North America. 2. European Article Number (EAN)."""

    isrc: Optional[str]
    """The International Standard Recording Code, abbreviated to ISRC, is a system of codes that identify audio and music video recordings."""

    disctitle: Optional[str]
    """Mediums are always included in a release, and have a position in said release (e.g. disc 1 or disc 2). They have a format, like CD, 12" vinyl or cassette (in some cases this will be unknown), and can have an optional title (e.g. disc 2: The Early Years)."""

    encoder: Optional[str]
    """The name of the person or organisation that encoded the audio file. This field may contain a copyright message, if the audio file also is copyrighted by the encoder."""

    script: Optional[str]
    """The script used to write the release’s track list. The possible values are taken from the ISO 15924 standard."""

    languages: Optional[list[str]]
    """The language a release’s track list is written in. The possible values are taken from the ISO 639-3 standard."""

    language: Optional[str]
    """The language a release’s track list is written in. The possible values are taken from the ISO 639-3 standard."""

    country: Optional[str]
    """The country the release was issued in."""

    albumstatus: Optional[str]
    """The status describes how "official" a release is."""

    media: Optional[str]
    """A prototypical medium is one of the physical, separate things you would get when you buy something in a record store."""

    albumdisambig: Optional[str]
    """The disambiguation album field helps to distinguish between identically named albums. The album “Weezer” for example has the disambiguation comments “Red Album” and “Green Album”."""

    # Release date.
    date: Optional[datetime.date]
    """The release date of the specific release."""

    year: Optional[int]
    """The release year of the specific release."""

    month: Optional[int]
    """The release month of the specific release."""

    day: Optional[int]
    """The release day of the specific release."""

    # *Original* release date.
    original_date: Optional[datetime.date]
    """The release date of the original version of the album."""

    original_year: Optional[int]
    """The release year of the original version of the album."""

    original_month: Optional[int]
    """The release month of the original version of the album."""

    original_day: Optional[int]
    """The release day of the original version of the album."""

    # Nonstandard metadata.
    artist_credit: Optional[str]
    """The track-specific artist credit name, which may be a variation of the artist’s “canonical” name."""

    artists_credit: Optional[list[str]]
    """The track-specific artists credit names, which may be a variation of the artist’s “canonical” names."""

    artists_sort: Optional[list[str]]
    """The “sort name” of the track artists."""

    albumartist_credit: Optional[str]
    """The release-specific artist credit name, which may be a variation of the artist’s “canonical” name"""

    albumartists_credit: Optional[list[str]]
    """The release-specific artists credit names, which may be a variation of the artist’s “canonical” names."""

    albumartists_sort: Optional[list[str]]
    """The “sort name” of the artist for the entire album."""

    # Legacy album art field
    art: Optional[bytes]
    """Legacy album art field."""

    # Image list
    images: Optional[list[Image]]
    """Cover art, also known as "album art" or "album artwork", is artwork that provides a visual representation of a release."""

    # MusicBrainz IDs.
    mb_trackid: Optional[str]
    """MusicBrainz track ID."""

    mb_releasetrackid: Optional[str]
    """MusicBrainz release track ID."""

    mb_workid: Optional[str]
    """MusicBrainz work ID."""

    mb_albumid: Optional[str]
    """MusicBrainz work ID."""

    mb_artistids: Optional[list[str]]
    """MusicBrainz artist IDs as a list."""

    mb_artistid: Optional[str]
    """MusicBrainz artist ID."""

    mb_albumartistids: Optional[list[str]]
    """MusicBrainz artist IDs as a list."""

    mb_albumartistid: Optional[str]
    """MusicBrainz album artist ID."""

    mb_releasegroupid: Optional[str]
    """MusicBrainz releasegroup ID."""

    # Acoustid fields.
    acoustid_fingerprint: Optional[str]
    """The Acoustic Fingerprint for the track. The fingerprint is based on the audio information found in a file, and is calculated using the Chromaprint software."""

    acoustid_id: Optional[str]
    """The AcoustID associated with the track. The AcoustID is the identifier assigned to an audio file based on its acoustic fingerprint. Multiple fingerprints may be assigned the same AcoustID if the fingerprints are similar enough."""

    # ReplayGain fields.
    rg_track_gain: Optional[float]
    """ReplayGain Track Gain, see https://en.wikipedia.org/wiki/ReplayGain."""

    rg_album_gain: Optional[float]
    """ReplayGain Album Gain, see https://en.wikipedia.org/wiki/ReplayGain."""

    rg_track_peak: Optional[float]
    """ReplayGain Track Peak, see https://en.wikipedia.org/wiki/ReplayGain."""

    rg_album_peak: Optional[float]
    """ReplayGain Album Peak, see https://en.wikipedia.org/wiki/ReplayGain."""

    # EBU R128 fields.
    r128_track_gain: Optional[float]
    """An optional gain for track normalization. EBU R 128 is a recommendation for loudness normalisation and maximum level of audio signals."""

    r128_album_gain: Optional[float]
    """An optional gain for album normalization. EBU R 128 is a recommendation for loudness normalisation and maximum level of audio signals."""

    initial_key: Optional[str]
    """The Initial key frame contains the musical key in which the sound starts. It is represented as a string with a maximum length of three characters. The ground keys are represented with "A","B","C","D","E", "F" and "G" and halfkeys represented with "b" and "#". Minor is represented as "m"."""

    @property
    def length(self) -> float:
        """The duration of the audio in seconds (a float)."""

    @property
    def samplerate(self) -> int:
        """The audio's sample rate (an int)."""

    @property
    def bitdepth(self) -> int:
        """The number of bits per sample in the audio encoding (an int).
        Only available for certain file formats (zero where
        unavailable).
        """

    @property
    def channels(self) -> int:
        """The number of channels in the audio (an int)."""

    @property
    def bitrate(self) -> int:
        """The number of bits per seconds used in the audio coding (an
        int). If this is provided explicitly by the compressed file
        format, this is a precise reflection of the encoding. Otherwise,
        it is estimated from the on-disk file size. In this case, some
        imprecision is possible because the file header is incorporated
        in the file size.
        """

    @property
    def bitrate_mode(self) -> Literal["CBR", "VBR", "ABR", ""]:
        """The mode of the bitrate used in the audio coding
        (a string, eg. "CBR", "VBR" or "ABR").
        Only available for the MP3 file format (empty where unavailable).
        """

    @property
    def encoder_info(self) -> str:
        """The name and/or version of the encoder used
        (a string, eg. "LAME 3.97.0").
        Only available for some formats (empty where unavailable).
        """

    @property
    def encoder_settings(self) -> str:
        """A guess of the settings used for the encoder (a string, eg. "-V2").
        Only available for the MP3 file format (empty where unavailable).
        """

    @property
    def format(self) -> str:
        """A string describing the file format/codec."""
