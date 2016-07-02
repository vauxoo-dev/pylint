# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""Module to check ungrouped isinstances methods for pylint. """

import astroid

from pylint import checkers, utils
from pylint.checkers.utils import check_messages
from pylint.interfaces import IAstroidChecker

MSGS = {
    'E2685': ("isinstances of '%s' are not grouped. "
              "Use 'isinstance(%s, (class1, class2, ...))' instead",
              "ungrouped-isinstances",
              "Used when isinstances are not grouped by object"),
}


class UngroupedIsinstancesChecker(checkers.BaseChecker):
    __implements__ = IAstroidChecker
    name = 'ungrouped_isinstances'
    msgs = MSGS

    @check_messages(*(MSGS.keys()))
    def visit_boolop(self, node):
        "Check ungrouped isinstances"
        first_args = [
            value.args[0].as_string()
            for value in node.values
            if isinstance(value, astroid.Call) and value.args and
            value.func.name == 'isinstance']
        for duplicated_name in utils.get_duplicated(first_args):
            self.add_message('ungrouped-isinstances', node=node,
                             args=(duplicated_name, duplicated_name))


def register(linter):
    """Required method to auto register this checker.

    :param linter: Main interface object for Pylint plugins
    :type linter: Pylint object
    """
    linter.register_checker(UngroupedIsinstancesChecker(linter))
