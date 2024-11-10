import datetime
import os
import shutil
import tempfile
from pathlib import Path

import phrydy
from phrydy.mediafile_extended import MediaFileExtended
from tests import helper


def get_file(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "files", name)


def copy_to_tmp(name: str) -> str:
    orig = get_file(name)
    tmp = os.path.join(tempfile.mkdtemp(), os.path.basename(orig))
    shutil.copyfile(orig, tmp)
    return tmp


class TestMediafileExtended:
    mediafile: MediaFileExtended = MediaFileExtended(copy_to_tmp("full.mp3"))

    class TestConstructor:
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
                "+rb",
            )
            mediafile = MediaFileExtended(file)
            assert "tests/files/real-world/Bach_Weihnachts.mp3" in mediafile.filename
            assert mediafile.path is None

    def test_common_fields(self) -> None:
        assert self.mediafile.title == "full"

    def test_method_readable_fields(self):
        self.maxDiff = None
        fields = MediaFileExtended.readable_fields()
        f = list(fields)
        f.sort()
        d = list(phrydy.doc_generator.fields.keys())
        d.sort()
        assert f == d

    def test_new_fields(self) -> None:
        value = "ef8e0ef9-491e-42df-bff9-f13981da30a7"

        for extension in [
            "aiff",
            "alac.m4a",
            "flac",
            "m4a",
            "mp3",
            "mpc",
            "ogg",
            "opus",
            "wma",
            "wv",
        ]:
            for field in [
                "mb_workhierarchy_ids",
                "mb_workid",
                "releasegroup_types",
                "work",
                "work_hierarchy",
            ]:
                tmp = copy_to_tmp("mb." + extension)
                orig = MediaFileExtended(tmp)
                setattr(orig, field, value)
                assert getattr(orig, field) == value
                orig.save()

                modified = MediaFileExtended(tmp)
                assert getattr(modified, field) == value, (
                    "field: " + field + ", extension: " + extension
                )

    def test_fields(self) -> None:
        assert list(self.mediafile.fields()) == [
            "title",
            "artist",
            "artists",
            "album",
            "genres",
            "genre",
            "lyricist",
            "composer",
            "composer_sort",
            "arranger",
            "grouping",
            "track",
            "tracktotal",
            "disc",
            "disctotal",
            "url",
            "lyrics",
            "comments",
            "copyright",
            "bpm",
            "comp",
            "albumartist",
            "albumartists",
            "albumtypes",
            "albumtype",
            "label",
            "artist_sort",
            "albumartist_sort",
            "asin",
            "catalognums",
            "catalognum",
            "barcode",
            "isrc",
            "disctitle",
            "encoder",
            "script",
            "languages",
            "language",
            "country",
            "albumstatus",
            "media",
            "albumdisambig",
            "date",
            "year",
            "month",
            "day",
            "original_date",
            "original_year",
            "original_month",
            "original_day",
            "artist_credit",
            "artists_credit",
            "artists_sort",
            "albumartist_credit",
            "albumartists_credit",
            "albumartists_sort",
            "art",
            "images",
            "mb_trackid",
            "mb_releasetrackid",
            "mb_workid",
            "mb_albumid",
            "mb_artistids",
            "mb_artistid",
            "mb_albumartistids",
            "mb_albumartistid",
            "mb_releasegroupid",
            "acoustid_fingerprint",
            "acoustid_id",
            "rg_track_gain",
            "rg_album_gain",
            "rg_track_peak",
            "rg_album_peak",
            "r128_track_gain",
            "r128_album_gain",
            "initial_key",
            "mb_workhierarchy_ids",
            "work",
            "work_hierarchy",
            "releasegroup_types",
        ]

    def test_sorted_fields(self) -> None:
        assert list(self.mediafile.sorted_fields()) == [
            "acoustid_fingerprint",
            "acoustid_id",
            "album",
            "albumartist",
            "albumartist_credit",
            "albumartist_sort",
            "albumartists",
            "albumartists_credit",
            "albumartists_sort",
            "albumdisambig",
            "albumstatus",
            "albumtype",
            "albumtypes",
            "arranger",
            "art",
            "artist",
            "artist_credit",
            "artist_sort",
            "artists",
            "artists_credit",
            "artists_sort",
            "asin",
            "barcode",
            "bpm",
            "catalognum",
            "catalognums",
            "comments",
            "comp",
            "composer",
            "composer_sort",
            "copyright",
            "country",
            "date",
            "year",
            "month",
            "day",
            "disc",
            "disctitle",
            "disctotal",
            "encoder",
            "genre",
            "genres",
            "grouping",
            "images",
            "initial_key",
            "isrc",
            "label",
            "language",
            "languages",
            "lyricist",
            "lyrics",
            "mb_albumartistid",
            "mb_albumartistids",
            "mb_albumid",
            "mb_artistid",
            "mb_artistids",
            "mb_releasegroupid",
            "mb_releasetrackid",
            "mb_trackid",
            "mb_workid",
            "media",
            "original_date",
            "original_year",
            "original_month",
            "original_day",
            "r128_album_gain",
            "r128_track_gain",
            "rg_album_gain",
            "rg_album_peak",
            "rg_track_gain",
            "rg_track_peak",
            "script",
            "title",
            "track",
            "tracktotal",
            "url",
        ]

    def test_readable_fields(self) -> None:
        assert list(self.mediafile.readable_fields()) == [
            "title",
            "artist",
            "artists",
            "album",
            "genres",
            "genre",
            "lyricist",
            "composer",
            "composer_sort",
            "arranger",
            "grouping",
            "track",
            "tracktotal",
            "disc",
            "disctotal",
            "url",
            "lyrics",
            "comments",
            "copyright",
            "bpm",
            "comp",
            "albumartist",
            "albumartists",
            "albumtypes",
            "albumtype",
            "label",
            "artist_sort",
            "albumartist_sort",
            "asin",
            "catalognums",
            "catalognum",
            "barcode",
            "isrc",
            "disctitle",
            "encoder",
            "script",
            "languages",
            "language",
            "country",
            "albumstatus",
            "media",
            "albumdisambig",
            "date",
            "year",
            "month",
            "day",
            "original_date",
            "original_year",
            "original_month",
            "original_day",
            "artist_credit",
            "artists_credit",
            "artists_sort",
            "albumartist_credit",
            "albumartists_credit",
            "albumartists_sort",
            "art",
            "images",
            "mb_trackid",
            "mb_releasetrackid",
            "mb_workid",
            "mb_albumid",
            "mb_artistids",
            "mb_artistid",
            "mb_albumartistids",
            "mb_albumartistid",
            "mb_releasegroupid",
            "acoustid_fingerprint",
            "acoustid_id",
            "rg_track_gain",
            "rg_album_gain",
            "rg_track_peak",
            "rg_album_peak",
            "r128_track_gain",
            "r128_album_gain",
            "initial_key",
            "mb_workhierarchy_ids",
            "work",
            "work_hierarchy",
            "releasegroup_types",
            "length",
            "samplerate",
            "bitdepth",
            "bitrate",
            "bitrate_mode",
            "channels",
            "encoder_info",
            "encoder_settings",
            "format",
        ]

    def test_as_dict(self) -> None:
        result = self.mediafile.as_dict()
        del result["art"]
        del result["images"]

        assert result == {
            "acoustid_fingerprint": None,
            "acoustid_id": None,
            "album": "the album",
            "albumartist": "the album artist",
            "albumartist_credit": None,
            "albumartist_sort": None,
            "albumartists": None,
            "albumartists_credit": None,
            "albumartists_sort": None,
            "albumdisambig": None,
            "albumstatus": None,
            "albumtype": None,
            "albumtypes": None,
            "arranger": None,
            "artist": "the artist",
            "artist_credit": None,
            "artist_sort": None,
            "artists": None,
            "artists_credit": None,
            "artists_sort": None,
            "asin": None,
            "barcode": None,
            "bpm": 6,
            "catalognum": None,
            "catalognums": None,
            "comments": "the comments",
            "comp": True,
            "composer": "the composer",
            "composer_sort": None,
            "copyright": None,
            "country": None,
            "date": datetime.date(2001, 1, 1),
            "day": None,
            "disc": 4,
            "disctitle": None,
            "disctotal": 5,
            "encoder": "iTunes v7.6.2",
            "genre": "the genre",
            "genres": ["the genre"],
            "grouping": "the grouping",
            "initial_key": None,
            "isrc": None,
            "label": "the label",
            "language": None,
            "languages": None,
            "lyricist": None,
            "lyrics": "the lyrics",
            "mb_albumartistid": None,
            "mb_albumartistids": None,
            "mb_albumid": "9e873859-8aa4-4790-b985-5a953e8ef628",
            "mb_artistid": "7cf0ea9d-86b9-4dad-ba9e-2355a64899ea",
            "mb_artistids": ["7cf0ea9d-86b9-4dad-ba9e-2355a64899ea"],
            "mb_releasegroupid": None,
            "mb_releasetrackid": "c29f3a57-b439-46fd-a2e2-93776b1371e0",
            "mb_trackid": "8b882575-08a5-4452-a7a7-cbb8a1531f9e",
            "mb_workhierarchy_ids": None,
            "mb_workid": None,
            "media": None,
            "month": None,
            "original_date": None,
            "original_day": None,
            "original_month": None,
            "original_year": None,
            "r128_album_gain": None,
            "r128_track_gain": None,
            "releasegroup_types": None,
            "rg_album_gain": None,
            "rg_album_peak": None,
            "rg_track_gain": 0.0,
            "rg_track_peak": 0.000244,
            "script": None,
            "title": "full",
            "track": 2,
            "tracktotal": 3,
            "url": None,
            "work": None,
            "work_hierarchy": None,
            "year": 2001,
        }
