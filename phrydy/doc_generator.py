import re
import textwrap
import typing
from typing import Any, Dict, Optional

import ansicolor

from .field_docs import FieldDoc, FieldDocCollection, fields
from .mediafile_extended import MediaFileExtended


def remove_color(text: str) -> str:
    """https://stackoverflow.com/a/14693789/10193818"""
    # 7-bit and 8-bit C1 ANSI sequences
    ansi_escape_8bit = re.compile(
        r"""
        (?: # either 7-bit C1, two bytes, ESC Fe (omitting CSI)
            \x1B
            [@-Z\\-_]
        |   # or a single 8-bit byte Fe (omitting CSI)
            [\x80-\x9A\x9C-\x9F]
        |   # or CSI + control codes
            (?: # 7-bit CSI, ESC [
                \x1B\[
            |   # 8-bit CSI, 9B
                \x9B
            )
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    """,
        re.VERBOSE,
    )
    return ansi_escape_8bit.sub("", text)


def get_type_name(t: typing.Any) -> str:
    return type(t).__name__


def print_dict_sorted(
    dictionary: typing.Dict[str, typing.Any],
    color: bool,
    align: typing.Literal["left", "right"] = "right",
) -> None:
    max_field_length = get_max_field_length(dictionary)

    for key, value in sorted(dictionary.items()):
        if align == "right":
            key = key.rjust(max_field_length, " ")
        elif align == "left":
            key = key.ljust(max_field_length, " ")
        key = key + ":"
        if color:
            key = ansicolor.green(key)
            value = value
        print(key + " " + value)


def print_section(text: str, color: bool = False) -> None:
    if color:
        text = ansicolor.blue(text.ljust(60, " "), reverse=True)
        line = ""
    else:
        line = "\n" + "".ljust(60, "-")

    print("\n" + text + line)


def print_debug(
    file_path: str,
    MediaClass: typing.Callable[[str], MediaFileExtended],
    field_generator: typing.Callable[[], typing.Generator[str, None, None]],
    color: bool = False,
) -> None:
    fields = MediaClass(file_path)

    # All class values
    print_section("All values provided by the class: " + MediaClass.__name__, color)

    class_fields = {}
    for key in field_generator():
        value = getattr(fields, key)
        if key == "art" and value:
            class_fields[key] = str(value[:95])
        else:
            class_fields[key] = str(value)

    print_dict_sorted(class_fields, color, align="left")

    # Raw mutagen values
    print_section("Raw mutagen values", color)

    mutagen_fields = {}
    for key, value in fields.mgfile.items():
        mutagen_fields[str(key)] = str(value)
    print_dict_sorted(mutagen_fields, color, align="left")

    # Class values
    print_section("Values provided by the class: " + MediaClass.__name__, color)

    class_fields = {}
    for key in field_generator():
        value = getattr(fields, key)
        if key != "art" and value:
            class_fields[key] = str(value)

    print_dict_sorted(class_fields, color, align="left")


def merge_fields(*fields: Any) -> FieldDocCollection:
    """Used in audiorename/args.py"""
    arguments = locals()
    out: FieldDocCollection = {}
    for fields in arguments["fields"]:
        out.update(fields)

    return out


def get_max_field_length(fields: Dict[str, Any]) -> int:
    """Get the length of the longest field in the dictionary ``fields``.

    :param dict fields: A dictionary to search for the longest field.
    """
    return max(map(len, fields))


FIELD_PREFIX = "$"
FIELD_SUFFIX = ":"
INDENT = 4


def format_field_as_txt(
    field_name: str, field_doc: FieldDoc, second_column: int, field_prefix: str = ""
) -> str:
    output = ""

    field_name_length = INDENT + len(field_prefix + field_name + FIELD_SUFFIX) + INDENT

    field_name = (
        " " * INDENT
        + ansicolor.cyan(field_prefix + field_name)
        + FIELD_SUFFIX
        + " " * INDENT
    )

    description_indent = " " * second_column

    description = field_doc["description"]
    output += (
        field_name
        + textwrap.fill(
            description,
            width=78,
            initial_indent=description_indent,
            subsequent_indent=description_indent,
        )[field_name_length:]
        + "\n"
    )

    if "examples" in field_doc:
        output += (
            description_indent
            + ansicolor.yellow("Examples:")
            + " "
            + str(field_doc["examples"])
            + "\n"
        )
    output += "\n\n"

    return output


def format_fields_as_txt(
    additional_fields: Optional[FieldDocCollection] = None,
    field_prefix: str = "",
    color: bool = False,
) -> str:
    """Return a formated string containing the documentation about the audio
    fields.
    """
    if additional_fields:
        f = fields.copy()
        f.update(additional_fields)
    else:
        f = fields

    # The beginning of the second column
    second_column = (
        INDENT
        + len(field_prefix)
        + get_max_field_length(f)
        + len(FIELD_SUFFIX)
        + INDENT
    )

    output = ""
    for field_name, field_doc in sorted(f.items()):
        output += format_field_as_txt(
            field_name, field_doc, second_column, field_prefix
        )
    if not color:
        output = remove_color(output)
    return output


FIRST_RST_CELL_PREFIX = "   * - "
RST_CELL_PREFIX = "     - "


def format_field_as_rst_table(field_name: str, field_doc: FieldDoc) -> str:
    output = FIRST_RST_CELL_PREFIX + field_name + "\n"
    output += RST_CELL_PREFIX + field_doc["category"] + "\n"
    output += RST_CELL_PREFIX + field_doc["description"] + "\n"
    if "examples" in field_doc:
        examples = field_doc["examples"].copy()
        examples_joined = ", ".join(list(map(lambda n: "``" + str(n) + "``", examples)))
        output += RST_CELL_PREFIX + examples_joined + "\n"
    else:
        output += RST_CELL_PREFIX + "\n"
    return output


def format_fields_as_rst_table(
    additional_fields: Optional[FieldDocCollection] = None,
) -> str:
    if additional_fields:
        f = fields.copy()
        f.update(additional_fields)
    else:
        f = fields

    header = """
.. list-table:: Fields documentation
   :widths: 20 10 50 20
   :header-rows: 1

   * - Field name
     - Category
     - Description
     - Examples
"""

    output = header
    for field_name, field_doc in sorted(f.items()):
        output += format_field_as_rst_table(field_name, field_doc)
    return output
