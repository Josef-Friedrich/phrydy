from . import field_docs  # noqa: F401
from . import doc_generator  # noqa: F401
from . import mediafile_extended  # noqa: F401
from ._version import get_versions
from .mediafile_extended import \
    MediaFile, \
    MediaFileExtended  # noqa: F401

from .field_docs import fields  # noqa: F401
from .doc_generator import format_fields_as_txt  # noqa: F401

__version__ = get_versions()['version']
del get_versions
