# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""Module to check not merged isinstance methods for pylint"""

import astroid

from pylint import checkers, utils
from pylint.checkers.utils import check_messages, is_builtin_object, safe_infer
from pylint.interfaces import IAstroidChecker

MSGS = {
    'R2685': ("isinstances of '%s' are not merged. "
              "Consider merging 'isinstance(%s, (class1, class2, ...))'",
              "consider-merging-isinstance",
              "Used when isinstances are not grouped by object"),
}


class ConsiderMergingIsinstanceChecker(checkers.BaseChecker):
    __implements__ = IAstroidChecker
    name = 'consider_merging_isinstance'
    msgs = MSGS

    @check_messages(*(MSGS.keys()))
    def visit_boolop(self, node):
        "Check not merged isinstance"
        if node.op != 'or':
            return
        first_args = [
            value.args[0].as_string()
            for value in node.values
            if isinstance(value, astroid.Call) and value.args and
            is_builtin_object(safe_infer(value.func)) and
            safe_infer(value.func).name == 'isinstance']
        for duplicated_name in utils.get_duplicated(first_args):
            self.add_message('consider-merging-isinstance', node=node,
                             args=(duplicated_name, duplicated_name))


def register(linter):
    """Required method to auto register this checker.

    :param linter: Main interface object for Pylint plugins
    :type linter: Pylint object
    """
    linter.register_checker(ConsiderMergingIsinstanceChecker(linter))
