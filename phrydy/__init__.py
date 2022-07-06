from typing import cast

from . import doc_generator, field_docs, mediafile_extended
from ._version import get_versions
from .doc_generator import (format_fields_as_txt, get_max_field_length,
                            merge_fields, print_debug)
from .field_docs import FieldDocCollection, fields
from .mediafile_extended import MediaFile, MediaFileExtended

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
