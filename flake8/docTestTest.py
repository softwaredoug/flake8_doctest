#!/usr/bin/env python


def foo(text):
    """ Print text
    >>> foo("bar")
    "bar"
    >>> foo("cat")
    "cat"
    """
    print "fail"

def passes(text):
    """ Print text
    >>> passes("foo")
    'foo'
    """
    return text


class Test:
    """
    >>> a=Test(5)
    >>> a.bar()
    50
    """

    def __init__(self, a):
        self.val = a

    def bar():
        print "fail"

if __name__ == "__main__":
    from doctest import testmod
    testmod()
