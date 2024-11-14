import enum
from collections.abc import Generator, Sequence
from io import BufferedRandom, BufferedReader
from pathlib import Path
from typing import Any, Optional, Union

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
    def __get__(self, mediafile, _): ...
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

    url: str
    lyrics: str
    comments: str
    copyright: str
    bpm: int
    comp: bool
    albumartist: str
    albumartists: list[str]
    albumtypes: list[str]
    albumtype: str
    label: str
    artist_sort: str
    albumartist_sort: str
    asin: str
    catalognums: list[str]
    catalognum: str
    barcode: int
    isrc: str
    disctitle: str
    encoder: str
    script: str
    languages: list[str]
    language: str
    country: str
    albumstatus: str
    media: str
    albumdisambig: str
    date: DateField
    year: int
    month: int
    day: int
    original_date: DateField
    original_year: int
    original_month: int
    original_day: int
    artist_credit: str
    artists_credit: list[str]
    artists_sort: list[str]
    albumartist_credit: str
    albumartists_credit: list[str]
    art: bytes
    images: list[Image]
    mb_trackid: str
    mb_releasetrackid: str
    mb_workid: str
    mb_albumid: str
    mb_artistids: list[str]
    mb_artistid: str
    mb_albumartistids: list[str]
    mb_albumartistid: str
    mb_releasegroupid: str
    acoustid_fingerprint: str
    acoustid_id: str
    rg_track_gain: float
    rg_album_gain: float
    rg_track_peak: float
    rg_album_peak: float
    r128_track_gain: float
    r128_album_gain: float
    initial_key: str

    mgfile: MutagenFile
