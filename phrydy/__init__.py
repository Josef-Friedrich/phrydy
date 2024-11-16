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


field_docs  # type: ignore

doc_generator  # type: ignore

mediafile_extended  # type: ignore

fields  # type: ignore

FieldDocCollection  # type: ignore

get_max_field_length  # type: ignore

format_fields_as_txt  # type: ignore

merge_fields  # type: ignore

print_debug  # type: ignore

MediaFile  # type: ignore

MediaFileExtended  # type: ignore
