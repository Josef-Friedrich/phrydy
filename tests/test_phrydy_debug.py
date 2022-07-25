"""Test the command line interface using subprocess."""

import os
import subprocess
import unittest


class TestCli(unittest.TestCase):
    def test_cli(self):
        output = subprocess.check_output(("phrydy-debug", "--help"))
        self.assertIn("usage: phrydy-debug", str(output))

        output = subprocess.check_output(
            ("phrydy-debug", os.path.join("tests", "files", "full.mp3"))
        )
        output = str(output)
        self.assertIn("Raw mutagen values", output)
        self.assertIn("COMM:iTunPGAP:eng                : 0", output)
        self.assertIn("TCMP                             : 1", output)
        self.assertIn("Values provided by the class: MediaFile", output)
        self.assertIn("title            : full", output)


if __name__ == "__main__":
    unittest.main()
