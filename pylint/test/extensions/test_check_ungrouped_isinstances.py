# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""Tests for the pylint checker in :mod:`pylint.extensions.check_ungrouped_isinstances
"""

import os.path as osp
import unittest

from pylint import checkers
from pylint.extensions.check_ungrouped_isinstances import register
from pylint.lint import PyLinter
from pylint.reporters import BaseReporter


class TestReporter(BaseReporter):

    def handle_message(self, msg):
        self.messages.append(msg)

    def on_set_current_module(self, module, filepath):
        self.messages = []


class TestUngroupedIsinstancesChecker(unittest.TestCase):
    """Test ungrouped isinstances Checker"""

    expected_msgs = [
        "isinstances of 'var3' are not grouped. "
        "Use 'isinstance(var3, (class1, class2, ...))' instead",
        "isinstances of 'var4' are not grouped. "
        "Use 'isinstance(var4, (class1, class2, ...))' instead",
        "isinstances of 'var5' are not grouped. "
        "Use 'isinstance(var5, (class1, class2, ...))' instead",
    ]

    @classmethod
    def setUpClass(cls):
        cls._linter = PyLinter()
        cls._linter.set_reporter(TestReporter())
        checkers.initialize(cls._linter)
        register(cls._linter)
        cls._linter.disable('all')
        cls._linter.enable('ungrouped-isinstances')

    def setUp(self):
        self.fname_example = osp.join(
            osp.dirname(osp.abspath(__file__)), 'data',
            'ungrouped_isinstances.py')

    def test_too_ungrouped_isinstances_message(self):
        self._linter.check([self.fname_example])
        real_msgs = [message.msg for message in self._linter.reporter.messages]
        self.assertEqual(sorted(self.expected_msgs), sorted(real_msgs))


if __name__ == '__main__':
    unittest.main()
