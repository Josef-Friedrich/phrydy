"""Test on real world meta data"""

import os
from pathlib import Path

from phrydy import MediaFileExtended
from tests import helper


class TestBachWeihnachts:
    mediafile = MediaFileExtended(
        os.path.join(helper.TEST_RESOURCES_PATH, "real-world/Bach_Weihnachts.mp3")
    )

    def test_constructor_path(self) -> None:
        mediafile = MediaFileExtended(
            Path(helper.TEST_RESOURCES_PATH) / "real-world" / "Bach_Weihnachts.mp3"
        )
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename

    def test_constructor_filelike_object(self) -> None:
        file = open(
            Path(helper.TEST_RESOURCES_PATH) / "real-world" / "Bach_Weihnachts.mp3",
            "rb",
        )
        mediafile = MediaFileExtended(file)
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename

    def test_filename(self) -> None:
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in self.mediafile.filename

    def test_title(self) -> None:
        assert (
            self.mediafile.title
            == 'Weihnachts-Oratorium, BWV 248: Teil I, I. Coro "Jauchzet, frohlocket!"'
        )
