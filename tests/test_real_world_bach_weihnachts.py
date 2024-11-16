"""Test on real world meta data: Bach Weihnachtsoratorium"""

import datetime

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

    # Field definitions.
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

    def test_url(self) -> None:
        assert self.mediafile.url is None

    def test_lyrics(self) -> None:
        assert self.mediafile.lyrics == "the lyrics"

    def test_comments(self) -> None:
        assert self.mediafile.comments == "the comments"

    def test_copyright(self) -> None:
        assert self.mediafile.copyright is None

    def test_bpm(self) -> None:
        assert self.mediafile.bpm == 6

    def test_comp(self) -> None:
        assert self.mediafile.comp is None

    def test_albumartist(self) -> None:
        assert (
            self.mediafile.albumartist
            == "Johann Sebastian Bach; Concentus Musicus Wien, Nikolaus Harnoncourt"
        )

    def test_albumartists(self) -> None:
        assert self.mediafile.albumartists is None

    def test_albumtypes(self) -> None:
        assert self.mediafile.albumtypes == ["album"]

    def test_albumtype(self) -> None:
        assert self.mediafile.albumtype == "album"

    def test_label(self) -> None:
        assert self.mediafile.label == "TELDEC"

    def test_artist_sort(self) -> None:
        assert self.mediafile.artist_sort == "Bach, Johann Sebastian"

    def test_albumartist_sort(self) -> None:
        assert (
            self.mediafile.albumartist_sort
            == "Bach, Johann Sebastian; Concentus Musicus Wien, Harnoncourt, Nikolaus"
        )

    def test_asin(self) -> None:
        assert self.mediafile.asin == "B000000SIC"

    def test_catalognums(self) -> None:
        assert self.mediafile.catalognums == ["9031776102"]

    def test_catalognum(self) -> None:
        assert self.mediafile.catalognum == "9031776102"

    def test_barcode(self) -> None:
        assert self.mediafile.barcode == "090317761022"

    def test_isrc(self) -> None:
        assert self.mediafile.isrc == "DEF056201641"

    def test_disctitle(self) -> None:
        assert self.mediafile.disctitle is None

    def test_encoder(self) -> None:
        assert self.mediafile.encoder == "iTunes v7.6.2"

    def test_script(self) -> None:
        assert self.mediafile.script == "Latn"

    def test_languages(self) -> None:
        assert self.mediafile.languages == ["deu"]

    def test_language(self) -> None:
        assert self.mediafile.language == "deu"

    def test_country(self) -> None:
        assert self.mediafile.country == "DE"

    def test_albumstatus(self) -> None:
        assert self.mediafile.albumstatus == "official"

    def test_media(self) -> None:
        assert self.mediafile.media == "CD"

    def test_albumdisambig(self) -> None:
        assert self.mediafile.albumdisambig is None

    # Release date.
    def test_date(self) -> None:
        assert self.mediafile.date == datetime.date(1992, 10, 26)

    def test_year(self) -> None:
        assert self.mediafile.year == 1992

    def test_month(self) -> None:
        assert self.mediafile.month == 10

    def test_day(self) -> None:
        assert self.mediafile.day == 26

    # *Original* release date.
    def test_original_date(self) -> None:
        assert self.mediafile.original_date == datetime.date(1992, 1, 1)

    def test_original_year(self) -> None:
        assert self.mediafile.original_year == 1992

    def test_original_month(self) -> None:
        assert self.mediafile.original_month is None

    def test_original_day(self) -> None:
        assert self.mediafile.original_day is None

    # Nonstandard metadata.
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

    def test_albumartists_sort(self) -> None:
        assert self.mediafile.albumartists_sort is None

    def test_art(self) -> None:
        assert self.mediafile.art is not None

    def test_images(self) -> None:
        assert self.mediafile.images is not None
