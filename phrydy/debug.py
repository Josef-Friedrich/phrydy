import argparse

from . import MediaFileExtended, __version__
from .doc_generator import format_fields_as_txt, print_debug


def description() -> str:
    """Build the description string."""
    return (
        """\
Debugging tool of the Python package “phrydy”, an easy \
wrapper around the “mutagen” library.
    """
        + "\n"
        + format_fields_as_txt(color=True)
    )


def init_cli() -> None:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=description()
    )

    parser.add_argument(
        "audio_file",
        help="A audio file",
    )

    parser.add_argument(
        "-c",
        "--color",
        help="Colorize the output",
        action="store_true",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )

    args = parser.parse_args()

    if args.audio_file:
        print("phrydy version " + __version__)

        print_debug(
            file_path=args.audio_file,
            MediaClass=MediaFileExtended,
            field_generator=MediaFileExtended.readable_fields,
            color=args.color,
        )
