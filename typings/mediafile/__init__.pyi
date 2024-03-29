"""
This type stub file was generated by pyright.
"""

from __future__ import absolute_import, division, print_function

import base64
import binascii
import codecs
import datetime
import enum
import functools
import imghdr
import logging
import math
import os
import re
import struct
import traceback

import mutagen
import mutagen._util
import mutagen.asf
import mutagen.flac
import mutagen.id3
import mutagen.mp3
import mutagen.mp4
import six

"""Handles low-level interfacing for files' tags. Wraps Mutagen to
automatically detect file types and provide a unified interface for a
useful subset of music files' tags.

Usage:

    >>> f = MediaFile('Lucy.mp3')
    >>> f.title
    'Lucy in the Sky with Diamonds'
    >>> f.artist = 'The Beatles'
    >>> f.save()

A field will always return a reasonable value of the correct type, even
if no tag is present. If no value is available, the value will be false
(e.g., zero or the empty string).

Internally ``MediaFile`` uses ``MediaField`` descriptors to access the
data from the tags. In turn ``MediaField`` uses a number of
``StorageStyle`` strategies to handle format specific logic.
"""
__version__ = ...
__all__ = ["UnreadableFileError", "FileTypeError", "MediaFile"]
log = ...
TYPES = ...
PREFERRED_IMAGE_EXTENSIONS = ...

class UnreadableFileError(Exception):
    """Mutagen is not able to extract information from the file."""

    def __init__(self, filename, msg) -> None: ...

class FileTypeError(UnreadableFileError):
    """Reading this type of file is not supported.

    If passed the `mutagen_type` argument this indicates that the
    mutagen type is not supported by `Mediafile`.
    """

    def __init__(self, filename, mutagen_type=...) -> None: ...

class MutagenError(UnreadableFileError):
    """Raised when Mutagen fails unexpectedly---probably due to a bug."""

    def __init__(self, filename, mutagen_exc) -> None: ...

def mutagen_call(action, filename, func, *args, **kwargs):
    """Call a Mutagen function with appropriate error handling.

    `action` is a string describing what the function is trying to do,
    and `filename` is the relevant filename. The rest of the arguments
    describe the callable to invoke.

    We require at least Mutagen 1.33, where `IOError` is *never* used,
    neither for internal parsing errors *nor* for ordinary IO error
    conditions such as a bad filename. Mutagen-specific parsing errors and IO
    errors are reraised as `UnreadableFileError`. Other exceptions
    raised inside Mutagen---i.e., bugs---are reraised as `MutagenError`.
    """
    ...

def loadfile(
    method=..., writable=..., create=...
):  # -> (func: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Unknown):
    """A decorator that works like `mutagen._util.loadfile` but with
    additional error handling.

    Opens a file and passes a `mutagen._utils.FileThing` to the
    decorated function. Should be used as a decorator for functions
    using a `filething` parameter.
    """
    ...

def image_mime_type(data):  # -> str:
    """Return the MIME type of the image data (a bytestring)."""
    ...

def image_extension(data): ...

class ImageType(enum.Enum):
    """Indicates the kind of an `Image` stored in a file's tag."""

    other = ...
    icon = ...
    other_icon = ...
    front = ...
    back = ...
    leaflet = ...
    media = ...
    lead_artist = ...
    artist = ...
    conductor = ...
    group = ...
    composer = ...
    lyricist = ...
    recording_location = ...
    recording_session = ...
    performance = ...
    screen_capture = ...
    fish = ...
    illustration = ...
    artist_logo = ...
    publisher_logo = ...

class Image:
    """Structure representing image data and metadata that can be
    stored and retrieved from tags.

    The structure has four properties.
    * ``data``  The binary data of the image
    * ``desc``  An optional description of the image
    * ``type``  An instance of `ImageType` indicating the kind of image
    * ``mime_type`` Read-only property that contains the mime type of
                    the binary data
    """

    def __init__(self, data, desc=..., type=...) -> None: ...
    @property
    def mime_type(self): ...
    @property
    def type_index(self): ...

class StorageStyle:
    """A strategy for storing a value for a certain tag format (or set
    of tag formats). This basic StorageStyle describes simple 1:1
    mapping from raw values to keys in a Mutagen file object; subclasses
    describe more sophisticated translations or format-specific access
    strategies.

    MediaFile uses a StorageStyle via three methods: ``get()``,
    ``set()``, and ``delete()``. It passes a Mutagen file object to
    each.

    Internally, the StorageStyle implements ``get()`` and ``set()``
    using two steps that may be overridden by subtypes. To get a value,
    the StorageStyle first calls ``fetch()`` to retrieve the value
    corresponding to a key and then ``deserialize()`` to convert the raw
    Mutagen value to a consumable Python value. Similarly, to set a
    field, we call ``serialize()`` to encode the value and then
    ``store()`` to assign the result into the Mutagen object.

    Each StorageStyle type has a class-level `formats` attribute that is
    a list of strings indicating the formats that the style applies to.
    MediaFile only uses StorageStyles that apply to the correct type for
    a given audio file.
    """

    formats = ...
    def __init__(
        self, key, as_type=..., suffix=..., float_places=..., read_only=...
    ) -> None:
        """Create a basic storage strategy. Parameters:

        - `key`: The key on the Mutagen file object used to access the
          field's data.
        - `as_type`: The Python type that the value is stored as
          internally (`unicode`, `int`, `bool`, or `bytes`).
        - `suffix`: When `as_type` is a string type, append this before
          storing the value.
        - `float_places`: When the value is a floating-point number and
          encoded as a string, the number of digits to store after the
          decimal point.
        - `read_only`: When true, writing to this field is disabled.
           Primary use case is so wrongly named fields can be addressed
           in a graceful manner. This does not block the delete method.

        """
        ...
    def get(self, mutagen_file):  # -> str | None:
        """Get the value for the field using this style."""
        ...
    def fetch(self, mutagen_file):  # -> None:
        """Retrieve the raw value of for this tag from the Mutagen file
        object.
        """
        ...
    def deserialize(self, mutagen_value):  # -> str:
        """Given a raw value stored on a Mutagen object, decode and
        return the represented value.
        """
        ...
    def set(self, mutagen_file, value):  # -> None:
        """Assign the value for the field using this style."""
        ...
    def store(self, mutagen_file, value):  # -> None:
        """Store a serialized value in the Mutagen file object."""
        ...
    def serialize(self, value):
        """Convert the external Python value to a type that is suitable for
        storing in a Mutagen file object.
        """
        ...
    def delete(self, mutagen_file):  # -> None:
        """Remove the tag from the file."""
        ...

class ListStorageStyle(StorageStyle):
    """Abstract storage style that provides access to lists.

    The ListMediaField descriptor uses a ListStorageStyle via two
    methods: ``get_list()`` and ``set_list()``. It passes a Mutagen file
    object to each.

    Subclasses may overwrite ``fetch`` and ``store``.  ``fetch`` must
    return a (possibly empty) list and ``store`` receives a serialized
    list of values as the second argument.

    The `serialize` and `deserialize` methods (from the base
    `StorageStyle`) are still called with individual values. This class
    handles packing and unpacking the values into lists.
    """

    def get(self, mutagen_file):  # -> str | None:
        """Get the first value in the field's value list."""
        ...
    def get_list(self, mutagen_file):  # -> list[str | Unknown]:
        """Get a list of all values for the field using this style."""
        ...
    def fetch(self, mutagen_file):  # -> list[Unknown]:
        """Get the list of raw (serialized) values."""
        ...
    def set(self, mutagen_file, value):  # -> None:
        """Set an individual value as the only value for the field using
        this style.
        """
        ...
    def set_list(self, mutagen_file, values):  # -> None:
        """Set all values for the field using this style. `values`
        should be an iterable.
        """
        ...
    def store(self, mutagen_file, values):  # -> None:
        """Set the list of all raw (serialized) values for this field."""
        ...

class SoundCheckStorageStyleMixin:
    """A mixin for storage styles that read and write iTunes SoundCheck
    analysis values. The object must have an `index` field that
    indicates which half of the gain/peak pair---0 or 1---the field
    represents.
    """

    def get(self, mutagen_file): ...
    def set(self, mutagen_file, value): ...

class ASFStorageStyle(ListStorageStyle):
    """A general storage style for Windows Media/ASF files."""

    formats = ...
    def deserialize(self, data): ...

class MP4StorageStyle(StorageStyle):
    """A general storage style for MPEG-4 tags."""

    formats = ...
    def serialize(self, value): ...

class MP4TupleStorageStyle(MP4StorageStyle):
    """A style for storing values as part of a pair of numbers in an
    MPEG-4 file.
    """

    def __init__(self, key, index=..., **kwargs) -> None: ...
    def deserialize(self, mutagen_value): ...
    def get(self, mutagen_file): ...
    def set(self, mutagen_file, value): ...
    def delete(self, mutagen_file): ...

class MP4ListStorageStyle(ListStorageStyle, MP4StorageStyle): ...

class MP4SoundCheckStorageStyle(SoundCheckStorageStyleMixin, MP4StorageStyle):
    def __init__(self, key, index=..., **kwargs) -> None: ...

class MP4BoolStorageStyle(MP4StorageStyle):
    """A style for booleans in MPEG-4 files. (MPEG-4 has an atom type
    specifically for representing booleans.)
    """

    def get(self, mutagen_file): ...
    def get_list(self, mutagen_file): ...
    def set(self, mutagen_file, value): ...
    def set_list(self, mutagen_file, values): ...

class MP4ImageStorageStyle(MP4ListStorageStyle):
    """Store images as MPEG-4 image atoms. Values are `Image` objects."""

    def __init__(self, **kwargs) -> None: ...
    def deserialize(self, data): ...
    def serialize(self, image): ...

class MP3StorageStyle(StorageStyle):
    """Store data in ID3 frames."""

    formats = ...
    def __init__(self, key, id3_lang=..., **kwargs) -> None:
        """Create a new ID3 storage style. `id3_lang` is the value for
        the language field of newly created frames.
        """
        ...
    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, value): ...

class MP3PeopleStorageStyle(MP3StorageStyle):
    """Store list of people in ID3 frames."""

    def __init__(self, key, involvement=..., **kwargs) -> None: ...
    def store(self, mutagen_file, value): ...
    def fetch(self, mutagen_file): ...

class MP3ListStorageStyle(ListStorageStyle, MP3StorageStyle):
    """Store lists of data in multiple ID3 frames."""

    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, values): ...

class MP3UFIDStorageStyle(MP3StorageStyle):
    """Store string data in a UFID ID3 frame with a particular owner."""

    def __init__(self, owner, **kwargs) -> None: ...
    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, value): ...

class MP3DescStorageStyle(MP3StorageStyle):
    """Store data in a TXXX (or similar) ID3 frame. The frame is
    selected based its ``desc`` field.
    ``attr`` allows to specify name of data accessor property in the frame.
    Most of frames use `text`.
    ``multispec`` specifies if frame data is ``mutagen.id3.MultiSpec``
    which means that the data is being packed in the list.
    """

    def __init__(
        self, desc=..., key=..., attr=..., multispec=..., **kwargs
    ) -> None: ...
    def store(self, mutagen_file, value): ...
    def fetch(self, mutagen_file): ...
    def delete(self, mutagen_file): ...

class MP3ListDescStorageStyle(MP3DescStorageStyle, ListStorageStyle):
    def __init__(self, desc=..., key=..., split_v23=..., **kwargs) -> None: ...
    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, values): ...

class MP3SlashPackStorageStyle(MP3StorageStyle):
    """Store value as part of pair that is serialized as a slash-
    separated string.
    """

    def __init__(self, key, pack_pos=..., **kwargs) -> None: ...
    def get(self, mutagen_file): ...
    def set(self, mutagen_file, value): ...
    def delete(self, mutagen_file): ...

class MP3ImageStorageStyle(ListStorageStyle, MP3StorageStyle):
    """Converts between APIC frames and ``Image`` instances.

    The `get_list` method inherited from ``ListStorageStyle`` returns a
    list of ``Image``s. Similarly, the `set_list` method accepts a
    list of ``Image``s as its ``values`` argument.
    """

    def __init__(self) -> None: ...
    def deserialize(self, apic_frame):  # -> Image:
        """Convert APIC frame into Image."""
        ...
    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, frames): ...
    def delete(self, mutagen_file): ...
    def serialize(self, image):
        """Return an APIC frame populated with data from ``image``."""
        ...

class MP3SoundCheckStorageStyle(SoundCheckStorageStyleMixin, MP3DescStorageStyle):
    def __init__(self, index=..., **kwargs) -> None: ...

class ASFImageStorageStyle(ListStorageStyle):
    """Store images packed into Windows Media/ASF byte array attributes.
    Values are `Image` objects.
    """

    formats = ...
    def __init__(self) -> None: ...
    def deserialize(self, asf_picture): ...
    def serialize(self, image): ...

class VorbisImageStorageStyle(ListStorageStyle):
    """Store images in Vorbis comments. Both legacy COVERART fields and
    modern METADATA_BLOCK_PICTURE tags are supported. Data is
    base64-encoded. Values are `Image` objects.
    """

    formats = ...
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file): ...
    def store(self, mutagen_file, image_data): ...
    def serialize(self, image):  # -> str:
        """Turn a Image into a base64 encoded FLAC picture block."""
        ...

class FlacImageStorageStyle(ListStorageStyle):
    """Converts between ``mutagen.flac.Picture`` and ``Image`` instances."""

    formats = ...
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file): ...
    def deserialize(self, flac_picture): ...
    def store(self, mutagen_file, pictures):  # -> None:
        """``pictures`` is a list of mutagen.flac.Picture instances."""
        ...
    def serialize(self, image):  # -> Picture:
        """Turn a Image into a mutagen.flac.Picture."""
        ...
    def delete(self, mutagen_file):  # -> None:
        """Remove all images from the file."""
        ...

class APEv2ImageStorageStyle(ListStorageStyle):
    """Store images in APEv2 tags. Values are `Image` objects."""

    formats = ...
    TAG_NAMES = ...
    def __init__(self) -> None: ...
    def fetch(self, mutagen_file): ...
    def set_list(self, mutagen_file, values): ...
    def delete(self, mutagen_file):  # -> None:
        """Remove all images from the file."""
        ...

class MediaField:
    """A descriptor providing access to a particular (abstract) metadata
    field.
    """

    def __init__(self, *styles, **kwargs) -> None:
        """Creates a new MediaField.

        :param styles: `StorageStyle` instances that describe the strategy
                       for reading and writing the field in particular
                       formats. There must be at least one style for
                       each possible file format.

        :param out_type: the type of the value that should be returned when
                         getting this property.

        """
        ...
    def styles(self, mutagen_file):  # -> Generator[Unknown, None, None]:
        """Yields the list of storage styles of this field that can
        handle the MediaFile's format.
        """
        ...
    def __get__(self, mediafile, owner=...): ...
    def __set__(self, mediafile, value): ...
    def __delete__(self, mediafile): ...

class ListMediaField(MediaField):
    """Property descriptor that retrieves a list of multiple values from
    a tag.

    Uses ``get_list`` and set_list`` methods of its ``StorageStyle``
    strategies to do the actual work.
    """

    def __get__(self, mediafile, _): ...
    def __set__(self, mediafile, values): ...
    def single_field(self):  # -> MediaField:
        """Returns a ``MediaField`` descriptor that gets and sets the
        first item.
        """
        ...

class DateField(MediaField):
    """Descriptor that handles serializing and deserializing dates

    The getter parses value from tags into a ``datetime.date`` instance
    and setter serializes such an instance into a string.

    For granular access to year, month, and day, use the ``*_field``
    methods to create corresponding `DateItemField`s.
    """

    def __init__(self, *date_styles, **kwargs) -> None:
        """``date_styles`` is a list of ``StorageStyle``s to store and
        retrieve the whole date from. The ``year`` option is an
        additional list of fallback styles for the year. The year is
        always set on this style, but is only retrieved if the main
        storage styles do not return a value.
        """
        ...
    def __get__(self, mediafile, owner=...): ...
    def __set__(self, mediafile, date): ...
    def __delete__(self, mediafile): ...
    def year_field(self): ...
    def month_field(self): ...
    def day_field(self): ...

class DateItemField(MediaField):
    """Descriptor that gets and sets constituent parts of a `DateField`:
    the month, day, or year.
    """

    def __init__(self, date_field, item_pos) -> None: ...
    def __get__(self, mediafile, _): ...
    def __set__(self, mediafile, value): ...
    def __delete__(self, mediafile): ...

class CoverArtField(MediaField):
    """A descriptor that provides access to the *raw image data* for the
    cover image on a file. This is used for backwards compatibility: the
    full `ImageListField` provides richer `Image` objects.

    When there are multiple images we try to pick the most likely to be a front
    cover.
    """

    def __init__(self) -> None: ...
    def __get__(self, mediafile, _): ...
    @staticmethod
    def guess_cover_image(candidates): ...
    def __set__(self, mediafile, data): ...
    def __delete__(self, mediafile): ...

class QNumberField(MediaField):
    """Access integer-represented Q number fields.

    Access a fixed-point fraction as a float. The stored value is shifted by
    `fraction_bits` binary digits to the left and then rounded, yielding a
    simple integer.
    """

    def __init__(self, fraction_bits, *args, **kwargs) -> None: ...
    def __get__(self, mediafile, owner=...): ...
    def __set__(self, mediafile, value): ...

class ImageListField(ListMediaField):
    """Descriptor to access the list of images embedded in tags.

    The getter returns a list of `Image` instances obtained from
    the tags. The setter accepts a list of `Image` instances to be
    written to the tags.
    """

    def __init__(self) -> None: ...

class MediaFile:
    """Represents a multimedia file on disk and provides access to its
    metadata.
    """

    @loadfile()
    def __init__(self, filething, id3v23=...) -> None:
        """Constructs a new `MediaFile` reflecting the provided file.

        `filething` can be a path to a file (i.e., a string) or a
        file-like object.

        May throw `UnreadableFileError`.

        By default, MP3 files are saved with ID3v2.4 tags. You can use
        the older ID3v2.3 standard by specifying the `id3v23` option.
        """
        ...
    @property
    def filename(self):
        """The name of the file.

        This is the path if this object was opened from the filesystem,
        or the name of the file-like object.
        """
        ...
    @filename.setter
    def filename(self, val):  # -> None:
        """Silently skips setting filename.
        Workaround for `mutagen._util._openfile` setting instance's filename.
        """
        ...
    @property
    def path(self):
        """The path to the file.

        This is `None` if the data comes from a file-like object instead
        of a filesystem path.
        """
        ...
    @property
    def filesize(self):  # -> int:
        """The size (in bytes) of the underlying file."""
        ...
    def save(self, **kwargs):  # -> None:
        """Write the object's tags back to the file.

        May throw `UnreadableFileError`. Accepts keyword arguments to be
        passed to Mutagen's `save` function.
        """
        ...
    def delete(self):  # -> None:
        """Remove the current metadata tag from the file. May
        throw `UnreadableFileError`.
        """
        ...
    @classmethod
    def fields(cls):  # -> Generator[str, None, None]:
        """Get the names of all writable properties that reflect
        metadata tags (i.e., those that are instances of
        :class:`MediaField`).
        """
        ...
    @classmethod
    def sorted_fields(cls):  # -> Generator[str, None, None]:
        """Get the names of all writable metadata fields, sorted in the
        order that they should be written.

        This is a lexicographic order, except for instances of
        :class:`DateItemField`, which are sorted in year-month-day
        order.
        """
        ...
    @classmethod
    def readable_fields(cls):  # -> Generator[str, None, None]:
        """Get all metadata fields: the writable ones from
        :meth:`fields` and also other audio properties.
        """
        ...
    @classmethod
    def add_field(cls, name, descriptor):  # -> None:
        """Add a field to store custom tags.

        :param name: the name of the property the field is accessed
                     through. It must not already exist on this class.

        :param descriptor: an instance of :class:`MediaField`.
        """
        ...
    def update(self, dict):  # -> None:
        """Set all field values from a dictionary.

        For any key in `dict` that is also a field to store tags the
        method retrieves the corresponding value from `dict` and updates
        the `MediaFile`. If a key has the value `None`, the
        corresponding property is deleted from the `MediaFile`.
        """
        ...
    def as_dict(self):  # -> dict[str, Any]:
        """Get a dictionary with all writable properties that reflect
        metadata tags (i.e., those that are instances of
        :class:`MediaField`).
        """
        ...
    title: str = ...
    artist: str = ...
    artists: str = ...
    album: str = ...
    genres: list[str] = ...
    genre: str = ...
    lyricist: str = ...
    composer: str = ...
    composer_sort: str = ...
    arranger: str = ...
    grouping: str = ...
    track: int = ...
    tracktotal: int = ...
    disc: int = ...
    disctotal: int = ...
    url: str = ...
    lyrics: str = ...
    comments: str = ...
    copyright: str = ...
    bpm: int = ...
    comp: bool = ...
    albumartist: str = ...
    albumartists: str = ...
    albumtype: str = ...
    label: str = ...
    artist_sort: str = ...
    albumartist_sort: str = ...
    asin: str = ...
    catalognum: str = ...
    barcode: int = ...
    isrc: str = ...
    disctitle: str = ...
    encoder: str = ...
    script: str = ...
    language: str = ...
    country: str = ...
    albumstatus: str = ...
    media: str = ...
    albumdisambig: str = ...
    date: int = ...
    year: int = ...
    month: int = ...
    day: int = ...
    original_date: str = ...
    original_year: int = ...
    original_month: int = ...
    original_day: int = ...
    artist_credit: str = ...
    albumartist_credit: str = ...
    art: bytes = ...
    images: list[Image] = ...
    mb_trackid: str = ...
    mb_releasetrackid: str = ...
    mb_workid: str = ...
    mb_albumid: str = ...
    mb_artistids: str = ...
    mb_artistid: str = ...
    mb_albumartistids: str = ...
    mb_albumartistid: str = ...
    mb_releasegroupid: str = ...
    acoustid_fingerprint: str = ...
    acoustid_id: str = ...
    rg_track_gain: float = ...
    rg_album_gain: float = ...
    rg_track_peak: float = ...
    rg_album_peak: float = ...
    r128_track_gain: float = ...
    r128_album_gain: float = ...
    initial_key: str = ...

    @property
    def length(self):
        """The duration of the audio in seconds (a float)."""
        ...
    @property
    def samplerate(self):  # -> Literal[48000, 0]:
        """The audio's sample rate (an int)."""
        ...
    @property
    def bitdepth(self):  # -> Literal[0]:
        """The number of bits per sample in the audio encoding (an int).
        Only available for certain file formats (zero where
        unavailable).
        """
        ...
    @property
    def channels(self):  # -> Literal[0]:
        """The number of channels in the audio (an int)."""
        ...
    @property
    def bitrate(self):  # -> int:
        """The number of bits per seconds used in the audio coding (an
        int). If this is provided explicitly by the compressed file
        format, this is a precise reflection of the encoding. Otherwise,
        it is estimated from the on-disk file size. In this case, some
        imprecision is possible because the file header is incorporated
        in the file size.
        """
        ...
    @property
    def bitrate_mode(self):  # -> str:
        """The mode of the bitrate used in the audio coding
        (a string, eg. "CBR", "VBR" or "ABR").
        Only available for the MP3 file format (empty where unavailable).
        """
        ...
    @property
    def encoder_info(self):  # -> Literal['']:
        """The name and/or version of the encoder used
        (a string, eg. "LAME 3.97.0").
        Only available for some formats (empty where unavailable).
        """
        ...
    @property
    def encoder_settings(self):  # -> Literal['']:
        """A guess of the settings used for the encoder (a string, eg. "-V2").
        Only available for the MP3 file format (empty where unavailable).
        """
        ...
    @property
    def format(self):  # -> str:
        """A string describing the file format/codec."""
        ...
