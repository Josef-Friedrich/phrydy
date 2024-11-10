from importlib import metadata

from phrydy import doc_generator, field_docs, mediafile_extended
from phrydy.doc_generator import (
    format_fields_as_txt,
    get_max_field_length,
    merge_fields,
    print_debug,
)
from phrydy.field_docs import FieldDocCollection, fields
from phrydy.mediafile_extended import (
    MediaFile,
    MediaFileExtended,
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

MediaFile  # type: ignore

MediaFileExtended  # type: ignore
