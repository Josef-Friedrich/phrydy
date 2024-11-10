"""Test on real world meta data"""

import os
from pathlib import Path

from phrydy import MediaFileExtended
from tests import helper


class TestBachWeihnachts:
    mediafile = MediaFileExtended(
        os.path.join(helper.TEST_RESOURCES_PATH, "real-world/Bach_Weihnachts.mp3")
    )

    path = Path(helper.TEST_RESOURCES_PATH) / "real-world" / "Bach_Weihnachts.mp3"

    def test_constructor_path(self) -> None:
        mediafile = MediaFileExtended(self.path)
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename

    def test_constructor_filelike_object_rb(self) -> None:
        file = open(
            self.path,
            "rb",
        )
        mediafile = MediaFileExtended(file)
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename
        assert mediafile.path is None

    def test_constructor_filelike_object_rb_plus(self) -> None:
        file = open(
            self.path,
            "rb+",
        )
        mediafile = MediaFileExtended(file)
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename
        assert mediafile.path is None

    def test_filename(self) -> None:
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in self.mediafile.filename

    def test_path(self) -> None:
        assert self.mediafile.path is not None
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in self.mediafile.path

    def test_title(self) -> None:
        assert (
            self.mediafile.title
            == 'Weihnachts-Oratorium, BWV 248: Teil I, I. Coro "Jauchzet, frohlocket!"'
        )
