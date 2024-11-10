"""Test on real world meta data: Bach Weihnachtsoratorium"""

from tests.helper import get_mediafile_extended


class TestBachWeihnachts:
    mediafile = get_mediafile_extended("real-world/Bach_Weihnachts.mp3")

    def test_filename(self) -> None:
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in self.mediafile.filename

    def test_path(self) -> None:
        assert self.mediafile.path is not None
        assert "tests/files/real-world/Bach_Weihnachts.mp3" in self.mediafile.path

    def test_filesize(self) -> None:
        assert self.mediafile.filesize == 93389

    def test_title(self) -> None:
        assert (
            self.mediafile.title
            == 'Weihnachts-Oratorium, BWV 248: Teil I, I. Coro "Jauchzet, frohlocket!"'
        )

    def test_artist(self) -> None:
        assert self.mediafile.artist == "Johann Sebastian Bach"

    def test_artists(self) -> None:
        assert self.mediafile.artists == ["Johann Sebastian Bach"]

    def test_album(self) -> None:
        assert self.mediafile.album == "Weihnachtsoratorium"

    def test_genres(self) -> None:
        assert self.mediafile.genres == ["the genre"]

    def test_genre(self) -> None:
        assert self.mediafile.genre == "the genre"

    def test_lyricist(self) -> None:
        assert self.mediafile.lyricist is None

    def test_composer(self) -> None:
        assert self.mediafile.composer == "Johann Sebastian Bach"

    def test_composer_sort(self) -> None:
        assert self.mediafile.composer_sort == "Bach, Johann Sebastian"

    def test_arranger(self) -> None:
        assert self.mediafile.arranger is None

    def test_grouping(self) -> None:
        assert self.mediafile.grouping == "the grouping"

    def test_track(self) -> None:
        assert self.mediafile.track == 1

    def test_tracktotal(self) -> None:
        assert self.mediafile.tracktotal == 33

    def test_disc(self) -> None:
        assert self.mediafile.disc == 1

    def test_disctotal(self) -> None:
        assert self.mediafile.disctotal == 2
