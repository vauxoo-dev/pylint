"""Checks use of "ungrouped-isinstances"""


def isinstances(self):
    "Examples of isinstances"
    var1, var2, var3, var4, var5 = 85

    # grouped
    if isinstance(var1, (int, long)):
        pass
    result = isinstance(var2, (int, long))

    # ungrouped
    if isinstance(var3, int) or isinstance(var3, long) or isinstance(var3, list) and True:
        pass
    result = isinstance(var4, int) or isinstance(var4, long) or isinstance(var5, list) and False
    result = isinstance(var4, int) or not isinstance(var4, long)
    result = isinstance(var5, int) or True or isinstance(var5, long)
