import re


def regString(pattern, string):
    result = re.search(pattern, string, re.S).span()
    result2 = re.match(pattern, string, re.I).span()
    return result, result2


def regString2(pattern, string):
    pattern = re.compile(pattern)
    result = pattern.findall(string)
    return result


