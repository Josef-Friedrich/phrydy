from typing import cast

from . import field_docs
from . import doc_generator
from . import mediafile_extended

from ._version import get_versions

from .mediafile_extended import \
    MediaFile, \
    MediaFileExtended

from .field_docs import \
    fields, \
    FieldDocCollection

from .doc_generator import \
    get_max_field_length, \
    format_fields_as_txt, \
    merge_fields, \
    print_debug

__version__: str = cast(str, get_versions()['version'])
del get_versions

field_docs

doc_generator

mediafile_extended

MediaFile

MediaFileExtended

fields

FieldDocCollection

get_max_field_length

format_fields_as_txt

merge_fields

print_debug
