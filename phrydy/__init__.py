from phrydy import field_docs  # noqa: F401
from phrydy import doc_generator  # noqa: F401
from phrydy import mediafile_extended  # noqa: F401
from phrydy._version import get_versions
from phrydy.mediafile_extended import \
    MediaFile, \
    MediaFileExtended  # noqa: F401

__version__ = get_versions()['version']
del get_versions
