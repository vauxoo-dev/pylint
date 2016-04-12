"""
Check that instantiating a class with `abc.ABCMeta` as ancestor fails if it
defines abstract methods.
"""

# pylint: disable=too-few-public-methods, missing-docstring, no-init, docstring-first-line-empty

import abc



class BadClass(abc.ABC):
    @abc.abstractmethod
    def test(self):
        pass

def main():
    """ do nothing """
    BadClass() # [abstract-class-instantiated]
