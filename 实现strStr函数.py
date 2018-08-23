# -*- coding = utf-8 -*-


def strStr(haystack, needle):
    """
    :type haystack:str
    :type needle: str
    :rtype: int
    """
    if len(haystack) == len(needle):
        if haystack == needle:
            return 0
        else:
            return -1
    for i in range(0, len(haystack)):
        k = i
        j = 0
        while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
            j += 1
            k += 1
        if j == len(needle):
            return i
    return -1 if needle else 0


if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))

    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))
