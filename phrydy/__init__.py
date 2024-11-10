from collections.abc import Generator
from importlib import metadata
from pathlib import Path
from typing import Any, Callable, Union

from phrydy import doc_generator, field_docs, mediafile_extended
from phrydy.doc_generator import (
    format_fields_as_txt,
    get_max_field_length,
    merge_fields,
    print_debug,
)
from phrydy.field_docs import FieldDocCollection, fields
from phrydy.mediafile import DateField, Image, MediaField
from phrydy.mediafile_extended import (
    MediaFile,  # type: ignore
    MediaFileExtended,  # type: ignore
    MgFile,
)

__version__: str = metadata.version("phrydy")


field_docs

doc_generator

mediafile_extended

fields

FieldDocCollection

get_max_field_length

format_fields_as_txt

merge_fields

print_debug


class _MediaFile:
    __call__: Callable[..., "_MediaFile"]

    __name__: str

    @property
    def filename(self) -> str:  # type: ignore
        """The name of the file.

        This is the path if this object was opened from the filesystem,
        or the name of the file-like object.
        """
        ...

    @property
    def path(self) -> str:  # type: ignore
        """The path to the file.

        This is `None` if the data comes from a file-like object instead
        of a filesystem path.
        """
        ...

    @property
    def filesize(self) -> int:  # type: ignore
        """The size (in bytes) of the underlying file."""

    def save(self, **kwargs: Any) -> None:
        """Write the object's tags back to the file.

        May throw `UnreadableFileError`. Accepts keyword arguments to be
        passed to Mutagen's `save` function.
        """

    def delete(self) -> None:
        """Remove the current metadata tag from the file. May
        throw `UnreadableFileError`.
        """

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

    title: str
    """
    The title of a audio file.
    """
    artist: str
    artists: list[str]
    album: str
    genres: list[str]
    genre: str
    lyricist: str
    composer: str
    composer_sort: str
    arranger: str
    grouping: str
    track: int
    tracktotal: int
    disc: int
    disctotal: int
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


class _MediaFileExtended(_MediaFile):
    __call__: Callable[..., "_MediaFileExtended"]
    albumartist_sort: str
    """Changed field. Uses TSO2"""

    composer_sort: str
    """Changed field. Uses MP3 description storage style composersortorder."""

    mb_workid: str
    """Changed Field: The MusicBrainz’ Work ID"""

    mb_workhierarchy_ids: str
    """
    All IDs in the work hierarchy. This field corresponds to the field
    ``work_hierarchy``. The top level work ID appears first. As separator a
    slash (``/``) is used.

    Example:

    ``e208c5f5-5d37-3dfc-ac0b-999f207c9e46``
    ``/``
    ``5adc213f-700a-4435-9e95-831ed720f348``
    ``/``
    ``eafec51f-47c5-3c66-8c36-a524246c85f8``
    """

    work: str
    """The last work in the work hierarchy."""

    work_hierarchy: str
    """
    The hierarchy of works: The top level work appears first. As separator is
    this string used: ``-->``

    Example:

    ``Die Zauberflöte, K. 620``
    ``-->``
    ``Die Zauberflöte, K. 620: Akt I``
    ``-->``
    ``Die Zauberflöte, K. 620: Act I, Scene II. No. 2 Aria "Was hör' ...``

    """

    releasegroup_types: str
    """This field collects all items in the MusicBrainz’ API related to
    type: ``type``, ``primary-type`` and``secondary-type-list``. Main usage
    of this field is to determine in a secure manner if the release is a
    soundtrack.

    .. code:: JSON

        "release-group": {
          "first-release-date": "1994-09-27",
          "secondary-type-list": [
            "Compilation",
            "Soundtrack"
          ],
          "primary-type": "Album",
          "title": "Pulp Fiction: Music From the Motion Picture",
          "type": "Soundtrack",
          "id": "1703cd63-9401-33c0-87c6-50c4ba2e0ba8"
        }

    """


MediaFile: _MediaFile  # type: ignore

MediaFileExtended: _MediaFileExtended  # type: ignore


def get_media_file(filething: Union[str, Path], id3v23: bool = False) -> _MediaFile:
    return MediaFile(filething, id3v23)


def get_media_file_extended(
    filething: Union[str, Path], id3v23: bool = False
) -> _MediaFileExtended:
    return MediaFileExtended(filething, id3v23)
