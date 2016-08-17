""" Test that superfluous else return are detected. """

# pylint:disable=invalid-name,missing-docstring,unused-variable

def foo1(x, y, z):
    if x:
        a = 1
        return y
    else:  # [superfluous-else-return]
        b = 2
        return z


def foo2(x, y, w, z):
    if x:
        a = 1
        return y
    elif z:  # [superfluous-else-return]
        b = 2
        return w
    else:  # [superfluous-else-return]
        c = 3
        return z


def foo3(x, y, z):
    if x:
        a = 1
        if y:
            b = 2
            return y
        else:  # [superfluous-else-return]
            c = 3
            return x
    else:  # [superfluous-else-return]
        d = 4
        return z


def bar1(x, y, z):
    if x:
        return y
    return z


def bar2(w, x, y, z):
    if x:
        return y
    elif z:
        a = 1
    else:
        return w


def bar3(x, y, z):
    if x:
        if z:
            return y
    else:
        return z
