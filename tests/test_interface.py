"""Test public api / interface"""

import os

import phrydy
from phrydy import MediaFileExtended
from tests import helper


class TestInterface:
    def test_mediafile_class_in_init(self) -> None:
        mediafile = MediaFileExtended(
            os.path.join(helper.TEST_RESOURCES_PATH, "full.mp3")
        )
        assert mediafile.title == "full"

    def test_import_phrydy_media_file(self) -> None:
        assert phrydy.MediaFile.__name__ == "MediaFile"

    def test_import_phrydy_media_file_extended(self) -> None:
        assert phrydy.MediaFileExtended.__name__ == "MediaFileExtended"

    def test_import_phrydy_format_fields_as_txt(self) -> None:
        assert phrydy.format_fields_as_txt.__name__ == "format_fields_as_txt"

    def test_module_import_mediafile(self) -> None:
        mediafile = MediaFileExtended(
            os.path.join(helper.TEST_RESOURCES_PATH, "full.mp3")
        )
        assert mediafile.title == "full"

    def test_module_import_doc(self) -> None:
        fields = phrydy.doc_generator.fields
        assert fields
