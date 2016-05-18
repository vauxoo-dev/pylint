"""Checks import position rule"""
# pylint: disable=unused-import,relative-import,ungrouped-imports,import-error,no-name-in-module,relative-beyond-top-level,undefined-variable
if x:
    import os
# To force a ImportError from checkers
from .nonexists import testing   # [wrong-import-position]
