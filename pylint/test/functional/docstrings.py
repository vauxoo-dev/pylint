# pylint: disable=R0201
# -1: [missing-docstring]
from __future__ import print_function

# +1: [empty-docstring]
def function0():
    """"""

# +1: [missing-docstring]
def function1(value):
    # missing docstring
    print(value)

def function2(value):
    """docstring"""
    print(value)

def function3(value):
    """docstring"""
    print(value)

# +1: [missing-docstring]
class AAAA(object):
    # missing docstring

##     class BBBB:
##         # missing docstring
##         pass

##     class CCCC:
##         """yeah !"""
##         def method1(self):
##             pass

##         def method2(self):
##             """ yeah !"""
##             pass

    # +1: [missing-docstring]
    def method1(self):
        pass

    def method2(self):
        """ yeah !"""
        pass

    # +1: [empty-docstring]
    def method3(self):
        """"""
        pass

    def __init__(self):
        pass

class DDDD(AAAA):
    """yeah !"""

    def __init__(self):
        AAAA.__init__(self)

    # +1: [empty-docstring]
    def method2(self):
        """"""
        pass

    def method3(self):
        pass

    # +1: [missing-docstring]
    def method4(self):
        pass

    # +1: [docstring-first-line-empty]
    def method5(self):
        """
        Test Docstring First Line Empty
        """
        pass

# pylint: disable=missing-docstring
def function4():
    pass

# pylint: disable=empty-docstring
def function5():
    """"""
    pass

def function6():
    """ I am a {} docstring.""".format("good")

# +1: [docstring-first-line-empty]
def function7():
    """
    Test Docstring First Line Empty 2
    """
    pass

# +1: [docstring-first-line-empty]
class FFFF(AAAA):
    """
    Test Docstring First Line Empty 3
    """

# +1: [bad-docstring-quotes]
    def method6(self):
        '''Test Triple Single Quotes docstring
        '''
        pass

# +1: [bad-docstring-quotes]
    def method7(self):
        "docstring"
        pass

# +1: [bad-docstring-quotes]
    def method8(self):
        'docstring'
        pass

    # pylint: disable=undefined-variable
    @check_messages('bad-open-mode', 'redundant-unittest-assert',
                    'deprecated-module')
    def method9(self):
        """Test OK"""
        pass
