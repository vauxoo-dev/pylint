# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""Tests for the pylint checker in :mod:`pylint.extensions.consider_merging_isinstance
"""

import os.path as osp
import unittest

from pylint import checkers
from pylint.extensions.check_consider_merging_isinstance import register
from pylint.lint import PyLinter
from pylint.reporters import BaseReporter


class TestReporter(BaseReporter):

    def handle_message(self, msg):
        self.messages.append(msg)

    def on_set_current_module(self, module, filepath):
        self.messages = []


class TestConsiderMergingIsinstanceChecker(unittest.TestCase):
    """Test consider merging isinstances Checker"""

    expected_msgs = [
        "isinstances of 'var3' are not merged. "
        "Consider merging 'isinstance(var3, (class1, class2, ...))'",
        "isinstances of 'var4' are not merged. "
        "Consider merging 'isinstance(var4, (class1, class2, ...))'",
        "isinstances of 'var5' are not merged. "
        "Consider merging 'isinstance(var5, (class1, class2, ...))'",
        "isinstances of 'var6' are not merged. "
        "Consider merging 'isinstance(var6, (class1, class2, ...))'",
    ]

    @classmethod
    def setUpClass(cls):
        cls._linter = PyLinter()
        cls._linter.set_reporter(TestReporter())
        checkers.initialize(cls._linter)
        register(cls._linter)
        cls._linter.disable('all')
        cls._linter.enable('consider-merging-isinstance')

    def setUp(self):
        self.fname_example = osp.join(
            osp.dirname(osp.abspath(__file__)), 'data',
            'consider_merging_isinstance.py')

    def test_consider_merging_isinstance_message(self):
        self._linter.check([self.fname_example])
        real_msgs = [message.msg for message in self._linter.reporter.messages]
        self.assertEqual(sorted(self.expected_msgs), sorted(real_msgs))


if __name__ == '__main__':
    unittest.main()
