#!/usr/bin/env python
# -*- coding: utf-8 -*-

from phrydy import MediaFile

media_file = MediaFile("../tests/files/full.mp3")

for key in MediaFile.readable_fields():
    value = getattr(media_file, key)
    if key != "art" and value:
        print("{}: {}".format(key, value))
