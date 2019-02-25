# -*- coding: utf-8 -*-

from phrydy import doc  # noqa: F401
from phrydy import mediafile  # noqa: F401
from phrydy import utils  # noqa: F401
from phrydy._version import get_versions
from phrydy.mediafile import MediaFile  # noqa: F401

__version__ = get_versions()['version']
del get_versions
