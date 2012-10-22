import os.path


def runDocTests(path):
    """ Run all doctests in the specified module, printing to stdout
        the failures"""
    absPath = os.path.abspath(path)
    relPath = os.path.relpath(absPath)
    import unittest
    import doctest
    import imp
    from flake8.parseDocTest import parseDocTestResult
    res = unittest.TestResult()
    mod = imp.load_source('mod', path)
    suite = doctest.DocTestSuite(mod)

    suite.run(res)
    for failure in res.failures:
        for decodedFailureLine in parseDocTestResult(failure[1]):
            print "%s:%i:1: Failed Doctest" % (relPath, decodedFailureLine)
    return len(res.failures) + len(res.errors)

if __name__ == "__main__":
    from sys import argv
    runDocTests(argv[1])
