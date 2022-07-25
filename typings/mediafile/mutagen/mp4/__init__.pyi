"""
This type stub file was generated by pyright.
"""

from io import BytesIO

from mutagen._util import BitReader, BitReaderError, cdata
from mutagen.aac import ProgramConfigElement

from ._atom import Atom, AtomError
from ._util import parse_full_atom

class ASEntryError(Exception): ...

class AudioSampleEntry:
    """Parses an AudioSampleEntry atom.

    Private API.

    Attrs:
        channels (int): number of channels
        sample_size (int): sample size in bits
        sample_rate (int): sample rate in Hz
        bitrate (int): bits per second (0 means unknown)
        codec (string):
            audio codec, either 'mp4a[.*][.*]' (rfc6381) or 'alac'
        codec_description (string): descriptive codec name e.g. "AAC LC+SBR"

    Can raise ASEntryError.
    """

    channels = ...
    sample_size = ...
    sample_rate = ...
    bitrate = ...
    codec = ...
    codec_description = ...
    def __init__(self, atom, fileobj) -> None: ...

class DescriptorError(Exception): ...

class BaseDescriptor:
    TAG = ...
    @classmethod
    def parse(cls, fileobj):  # -> Self@BaseDescriptor:
        """Returns a parsed instance of the called type.
        The file position is right after the descriptor after this returns.

        Raises DescriptorError
        """
        ...

class ES_Descriptor(BaseDescriptor):
    TAG = ...
    def __init__(self, fileobj, length) -> None:
        """Raises DescriptorError"""
        ...

class DecoderConfigDescriptor(BaseDescriptor):
    TAG = ...
    decSpecificInfo = ...
    def __init__(self, fileobj, length) -> None:
        """Raises DescriptorError"""
        ...
    @property
    def codec_param(self):  # -> str:
        """string"""
        ...
    @property
    def codec_desc(self):  # -> str | None:
        """string or None"""
        ...

class DecoderSpecificInfo(BaseDescriptor):
    TAG = ...
    _TYPE_NAMES = ...
    _FREQS = ...
    @property
    def description(self):  # -> str | None:
        """string or None if unknown"""
        ...
    @property
    def sample_rate(self):  # -> int:
        """0 means unknown"""
        ...
    @property
    def channels(self):  # -> Any | Literal[0, 2, 1, 8] | None:
        """channel count or 0 for unknown"""
        ...
    def __init__(self, fileobj, length) -> None:
        """Raises DescriptorError"""
        ...

def GASpecificConfig(r, info):
    """Reads GASpecificConfig which is needed to get the data after that
    (there is no length defined to skip it) and to read program_config_element
    which can contain channel counts.

    May raise BitReaderError on error or
    NotImplementedError if some reserved data was set.
    """
    ...
