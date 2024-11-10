"""Test on real world meta data: no meta data"""

from tests.helper import get_mediafile_extended


class TestNoMeta:
    mediafile = get_mediafile_extended("real-world/Sex-Pistols_God-save-the-Queen.mp3")

    def test_filename(self) -> None:
        assert (
            "tests/files/real-world/Sex-Pistols_God-save-the-Queen.mp3"
            in self.mediafile.filename
        )

    def test_path(self) -> None:
        assert self.mediafile.path is not None
        assert (
            "tests/files/real-world/Sex-Pistols_God-save-the-Queen.mp3"
            in self.mediafile.path
        )

    def test_filesize(self) -> None:
        assert self.mediafile.filesize == 14656

    def test_title(self) -> None:
        assert self.mediafile.title == "God Save the Queen"

    def test_artist(self) -> None:
        assert self.mediafile.artist == "Sex Pistols"

    def test_artists(self) -> None:
        assert self.mediafile.artists == ["Sex Pistols"]

    def test_album(self) -> None:
        assert self.mediafile.album == "Never Mind the Bollocks Here's the Sex Pistols"

    def test_genres(self) -> None:
        assert self.mediafile.genres == ["the genre"]

    def test_genre(self) -> None:
        assert self.mediafile.genre == "the genre"

    def test_lyricist(self) -> None:
        assert self.mediafile.lyricist is None
