"""Checks import order rule with nested non_import sentence"""
# pylint: disable=unused-import,relative-import,ungrouped-imports,import-error,no-name-in-module,relative-beyond-top-level
try:
    # imports nested is a non_import sentence
    from sys import argv
except ImportError:
    pass

import os  # [wrong-import-position]
