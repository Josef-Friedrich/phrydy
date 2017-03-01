# -*- coding: utf-8 -*-

from .mediafile import MediaFile

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

MediaFile
