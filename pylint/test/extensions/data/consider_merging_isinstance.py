"""Checks use of consider-merging-isinstance"""


def isinstances(self):
    "Examples of isinstances"
    var1, var2, var3, var4, var5, var6 = 85

    # merged
    if isinstance(var1, (int, long)):
        pass
    result = isinstance(var2, (int, long))

    # not merged
    if isinstance(var3, int) or isinstance(var3, long) or isinstance(var3, list) and True:
        pass
    result = isinstance(var4, int) or isinstance(var4, long) or isinstance(var5, list) and False
    result = isinstance(var4, int) or not isinstance(var4, long)
    result = isinstance(var5, int) or True or isinstance(var5, long)

    infered_isinstance = isinstance
    result = infered_isinstance(var6, int) or infered_isinstance(var6, long) or infered_isinstance(var6, list) and False
