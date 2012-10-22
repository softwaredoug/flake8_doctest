import os.path
from functools import partial


def setUp(path, dTest):
    import imp
    print "Setup"
    print "path %s" % path
    mod = imp.load_source('mod', path)
    dTest.globs = dict(dTest.globs.items() + mod.__dict__.items())
    print dTest.globs
    #print type(mod)
    #from mod import *

    #dir(mod)


def runDocTests(path):
    """ Run all doctests in the specified module, printing to stdout
        the failures"""
    absPath = os.path.abspath(path)
    relPath = os.path.relpath(absPath)
    import unittest
    import doctest
    from flake8.parseDocTest import parseDocTestResult
    res = unittest.TestResult()
    print "Running test on %s" % relPath
    partialSetUp = partial(setUp, relPath)
    suite = doctest.DocFileSuite(relPath, module_relative=False,
                                 setUp=partialSetUp)

    suite.run(res)
    for failure in res.failures:
        print failure[1]
        for decodedFailureLine in parseDocTestResult(failure[1]):
            print "%s:%i:1: Failed Doctest" % (relPath, decodedFailureLine)
    return len(res.failures) + len(res.errors)

if __name__ == "__main__":
    from sys import argv
    runDocTests(argv[1])
