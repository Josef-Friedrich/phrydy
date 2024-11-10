"""Test on real world meta data: no meta data"""

from tests.helper import get_mediafile_extended


class TestNoMeta:
    mediafile = get_mediafile_extended("real-world/no_meta.mp3")

    def test_filename(self) -> None:
        assert "tests/files/real-world/no_meta.mp3" in self.mediafile.filename

    def test_path(self) -> None:
        assert self.mediafile.path is not None
        assert "tests/files/real-world/no_meta.mp3" in self.mediafile.path

    def test_filesize(self) -> None:
        assert self.mediafile.filesize == 10710

    def test_title(self) -> None:
        assert self.mediafile.title is None

    def test_artist(self) -> None:
        assert self.mediafile.artist is None

    def test_artists(self) -> None:
        assert self.mediafile.artists is None

    def test_album(self) -> None:
        assert self.mediafile.album is None

    def test_genres(self) -> None:
        assert self.mediafile.genres is None

    def test_genre(self) -> None:
        assert self.mediafile.genre is None

    def test_lyricist(self) -> None:
        assert self.mediafile.lyricist is None

    def test_composer(self) -> None:
        assert self.mediafile.composer is None

    def test_composer_sort(self) -> None:
        assert self.mediafile.composer_sort is None

    def test_arranger(self) -> None:
        assert self.mediafile.arranger is None

    def test_grouping(self) -> None:
        assert self.mediafile.grouping is None

    def test_track(self) -> None:
        assert self.mediafile.track is None

    def test_tracktotal(self) -> None:
        assert self.mediafile.tracktotal is None

    def test_disc(self) -> None:
        assert self.mediafile.disc is None

    def test_disctotal(self) -> None:
        assert self.mediafile.disctotal is None
