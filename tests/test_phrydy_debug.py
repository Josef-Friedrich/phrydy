"""Test the command line interface using subprocess."""

import os
import subprocess


def test_cli() -> None:
    output: str = subprocess.check_output(("phrydy-debug", "--help"), encoding="utf-8")
    assert "usage: phrydy-debug" in str(output)

    output = subprocess.check_output(
        ("phrydy-debug", os.path.join("tests", "files", "full.mp3")), encoding="utf-8"
    )
    assert "Raw mutagen values" in output
    assert "COMM:iTunPGAP:eng                : 0" in output
    assert "TCMP                             : 1" in output
    assert "Values provided by the class: MediaFile" in output
    assert "title            : full" in output
