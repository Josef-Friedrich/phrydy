from collections.abc import Generator
from io import BufferedRandom, BufferedReader
from pathlib import Path
from typing import Any, Optional, Union

from mediafile import DateField, Image, MediaField

from phrydy.mediafile_extended import MgFile

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

    mgfile: MgFile
