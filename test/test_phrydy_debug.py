# -*- coding: utf-8 -*-

"""Test the command line interface using subprocess."""

import subprocess
import unittest


class TestCli(unittest.TestCase):

    def test_cli(self):
        output = subprocess.check_output(('phrydy-debug', '--help'))
        self.assertTrue('usage: phrydy-debug' in str(output))


if __name__ == '__main__':
    unittest.main()