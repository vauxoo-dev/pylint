# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""check to consider a refactory of code"""

import collections

import astroid

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages, is_builtin_object, safe_infer


MSGS = {
    'R1701': (
        "isinstances of '%s' are not merged. "
        "Consider merging 'isinstance(%s, (class1, class2, ...))'",
        "consider-merging-isinstance",
        "Used when isinstance methods are not grouped by object"),
}


def get_duplicated(items):
    """Get duplicated items
    :param iter items: Items to extract duplicated
    :returns: Duplicated items retrieved from the given argument.
    :rtype: list
    """
    items_counter = collections.Counter(items)
    return [item for item, counter in items_counter.items() if counter > 1]


class RefactoryChecker(BaseChecker):
    """Checks to consider a refactory of code
    * isinstance merging
    """

    __implements__ = (IAstroidChecker,)

    # configuration section name
    name = 'refactory'

    msgs = MSGS
    priority = -2

    def _get_first_args(self, node):
        """Get first item of all node.args as string of method 'isinstance'.
        :param astroid.BoolOp node: Node to get first argument of values
        :returns: First arguments as string of all `node.values`
        :rtype: generator
        """
        for value in node.values:
            if not isinstance(value, astroid.Call) or not value.args:
                continue
            inferred = safe_infer(value.func)
            if not inferred or not is_builtin_object(inferred):
                continue
            if inferred.name == 'isinstance':
                yield value.args[0].as_string()

    @check_messages(*(MSGS.keys()))
    def visit_boolop(self, node):
        "Check not merged isinstance"
        if node.op != 'or':
            return
        first_args = [first_arg for first_arg in self._get_first_args(node)]
        for duplicated_name in get_duplicated(first_args):
            self.add_message('consider-merging-isinstance', node=node,
                             args=(duplicated_name, duplicated_name))


def register(linter):
    """required method to auto register this checker """
    linter.register_checker(RefactoryChecker(linter))
