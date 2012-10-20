def parseFailDetails(failDetails):
    """ Parse the line number of the doctest failure"""
    import re
    failDetails = failDetails.split(',')
    lineNo = -1
    if len(failDetails) == 3:
        match = re.search("line.*?(\d+)", failDetails[1])
        if match is None:
            return lineNo
        lineNo = int(match.group(1))
    return lineNo


def parseDocTestResult(docTestResStr):
    """ Extract the line number and filename of the doctest failure"""
    lines = docTestResStr.split("\n")
    for lineNo, line in enumerate(lines):
        failure = line.find("Failed example:")
        if failure != -1:
            failDetails = lines[lineNo - 1]
            yield parseFailDetails(failDetails)
