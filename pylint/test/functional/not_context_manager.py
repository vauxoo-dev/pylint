"""Tests that onjects used in a with statement implement context manager protocol"""

# pylint: disable=too-few-public-methods, invalid-name, import-error, missing-docstring

# Tests no messages for objects that implement the protocol
class Manager(object):
    def __enter__(self):
        pass
    def __exit__(self, type_, value, traceback):
        pass
with Manager():
    pass

class AnotherManager(Manager):
    pass
with AnotherManager():
    pass


# Tests message for class that doesn't implement the protocol
class NotAManager(object):
    pass
with NotAManager():  #[not-context-manager]
    pass

# Tests contextlib.contextmanager usage is recognized as correct.
from contextlib import contextmanager
@contextmanager
def dec():
    yield
with dec():  # valid use
    pass


# Tests a message is produced when a contextlib.contextmanager
# decorated function is used without being called.
with dec:  # [not-context-manager]
    pass


# Tests no messages about context manager protocol
# if the type can't be inferred.
from missing import Missing
with Missing():
    pass