"""
This type stub file was generated by pyright.
"""

import sys
import warnings
from importlib import import_module
from typing import Any, Dict

"""
    sphinx.deprecation
    ~~~~~~~~~~~~~~~~~~

    Sphinx deprecation classes and utilities.

    :copyright: Copyright 2007-2020 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
if False: ...

class RemovedInSphinx40Warning(DeprecationWarning): ...
class RemovedInSphinx50Warning(PendingDeprecationWarning): ...

RemovedInNextVersionWarning = RemovedInSphinx40Warning

def deprecated_alias(
    modname: str,
    objects: Dict[str, object],
    warning: Type[Warning],
    names: Dict[str, str] = ...,
) -> None: ...

class _ModuleWrapper:
    def __init__(
        self,
        module: Any,
        modname: str,
        objects: Dict[str, object],
        warning: Type[Warning],
        names: Dict[str, str],
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class DeprecatedDict(dict):
    """A deprecated dict which warns on each access."""

    def __init__(self, data: Dict, message: str, warning: Type[Warning]) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def setdefault(self, key: str, default: Any = ...) -> Any: ...
    def __getitem__(self, key: str) -> None: ...
    def get(self, key: str, default: Any = ...) -> Any: ...
    def update(self, other: Dict) -> None: ...
