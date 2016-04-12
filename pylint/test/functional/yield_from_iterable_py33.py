"""
Check that `yield from`-statement takes an iterable.
"""
# pylint: disable=missing-docstring,docstring-first-line-empty

def to_ten():
    yield from 10  # [not-an-iterable]
