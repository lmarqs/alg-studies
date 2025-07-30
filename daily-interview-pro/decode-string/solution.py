def decodeString(str):
    substr = decodeSubstring(str, 0, len(str) - 1)
    return substr


def decodeSubstring(str, start, end):
    ob = findOpeningBracket(str, start, end)

    if ob == -1:
        return str[start : end + 1]

    cb = findClosingBracket(str, start, end)

    substr = decodeSubstring(str, ob + 1, cb - 1)

    return str[start : ob - 1] + int(str[ob - 1]) * substr + str[cb + 1 : end + 1]


def findOpeningBracket(str, start, end):
    idx = start
    while idx <= end:
        if str[idx] == "[":
            return idx
        idx += 1
    return -1


def findClosingBracket(str, start, end):
    idx = end
    while idx >= start:
        if str[idx] == "]":
            return idx
        idx -= 1
    return -1
