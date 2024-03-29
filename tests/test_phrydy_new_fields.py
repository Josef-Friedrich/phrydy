"""Test additional meta fields not included in beets MediaFileExtended."""

import os
import shutil
import tempfile

from phrydy import MediaFileExtended


def get_file(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "files", name)


def copy_to_tmp(name: str) -> str:
    orig: str = get_file(name)
    tmp: str = os.path.join(tempfile.mkdtemp(), os.path.basename(orig))
    shutil.copyfile(orig, tmp)
    return tmp


def test_new_fields() -> None:
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
