"""Automatically-generated blanket testing for the MediaFileExtended metadata
layer.
"""

import os

from stdout_stderr_capturing import Capturing

import phrydy
from phrydy.field_docs import FieldDoc
from phrydy.mediafile_extended import MediaFileExtended


class TestPrintDebug:
    def test_print_debug(self) -> None:
        with Capturing() as output:
            phrydy.doc_generator.print_debug(
                os.path.join(os.path.dirname(__file__), "files", "full.mp3"),
                MediaFileExtended,
                MediaFileExtended.readable_fields,
                False,
            )

        assert output[-1] == "year             : 2001"


class TestDoc:
    def test_field(self) -> None:
        assert phrydy.field_docs.fields

    def test_field_title(self) -> None:
        assert phrydy.field_docs.fields["artist"]["description"]

    def test_field_category(self) -> None:
        assert phrydy.field_docs.fields["artist"]["category"]

    def test_field_long_title(self) -> None:
        title = phrydy.field_docs.fields["catalognum"]["description"]
        assert len(title) > 100
        assert "number assigned" in title

    def test_doc_string(self) -> None:
        assert isinstance(phrydy.format_fields_as_txt(), str)

    def test_doc_length(self) -> None:
        assert len(phrydy.format_fields_as_txt()) > 1000

    def test_get_max_field_lengths(self) -> None:
        tmp = phrydy.doc_generator.fields.copy()
        field_doc: FieldDoc = {"description": "Description", "category": "common"}
        tmp["looooooooooooooooooooooooooooooooooooooong"] = field_doc
        length = phrydy.doc_generator.get_max_field_length(tmp)
        assert length == 42

    def test_get_additional_docs(self) -> None:
        fields: phrydy.doc_generator.FieldDocCollection = {
            "lol": {
                "description": "loool",
                "category": "common",
            },
        }
        output = phrydy.doc_generator.format_fields_as_txt(additional_fields=fields)
        assert "loool" in output

    def test_field_order(self) -> None:
        output = phrydy.doc_generator.format_fields_as_txt().split("\n")
        assert "acoustid_fingerprint" in output[0]

    def test_all_fields_are_documented(self) -> None:
        for field in MediaFileExtended.fields():
            assert phrydy.doc_generator.fields.get(field), field

    def test_function_merge_fields(self) -> None:
        field1 = {
            "title": {
                "description": "The title of a audio file.",
                "category": "ordinary",
            },
        }
        field2 = {
            "arranger": {
                "description": "arranger",
                "category": "ordinary",
            },
        }
        out = phrydy.doc_generator.merge_fields(field1, field2)
        assert out["arranger"]["description"] == "arranger"
        assert out["title"]["description"] == "The title of a audio file."
