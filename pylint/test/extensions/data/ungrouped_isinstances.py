"""Checks use of "ungrouped-isinstances"""


def isinstances(self):
    "Examples of isinstances"
    var1, var2, var3, var4 = 85

    # grouped
    if isinstance(var1, (int, long)):
        pass
    result = isinstance(var2, (int, long))

    # ungrouped
    if isinstance(var3, int) or isinstance(var3, long):
        pass
    result = isinstance(var4, int) or isinstance(var4, long)
