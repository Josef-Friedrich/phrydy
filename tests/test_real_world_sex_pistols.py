"""Test on real world meta data: no meta data"""

import datetime

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

    def test_date(self) -> None:
        assert self.mediafile.date == datetime.date(1996, 6, 24)

    def test_year(self) -> None:
        assert self.mediafile.year == 1996

    def test_month(self) -> None:
        assert self.mediafile.month == 6

    def test_day(self) -> None:
        assert self.mediafile.day == 24

    def test_original_date(self) -> None:
        assert self.mediafile.original_date == datetime.date(1977, 1, 1)

    def test_original_year(self) -> None:
        assert self.mediafile.original_year == 1977

    def test_original_month(self) -> None:
        assert self.mediafile.original_month is None

    def test_original_day(self) -> None:
        assert self.mediafile.original_day is None

    def test_artist_credit(self) -> None:
        assert self.mediafile.artist_credit is None

    def test_artists_credit(self) -> None:
        assert self.mediafile.artists_credit is None

    def test_artists_sort(self) -> None:
        assert self.mediafile.artists_sort is None

    def test_albumartist_credit(self) -> None:
        assert self.mediafile.albumartist_credit is None

    def test_albumartists_credit(self) -> None:
        assert self.mediafile.albumartists_credit is None

    def test_art(self) -> None:
        assert self.mediafile.art is None

    def test_images(self) -> None:
        assert self.mediafile.images is None
