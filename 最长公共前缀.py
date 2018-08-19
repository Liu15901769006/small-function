# -*- coding = utf-8 -*-


def longestCommonPrefix(strs):
    """
    :type strs: list
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    str = strs[0]
    min = len(str)
    for i in range(1, len(strs)):
        j = 0
        p = strs[i]
        while j < min and j < len(p) and p[j] == str[j]:
            j += 1
        min = min if min < j else j
    return str[:min]


if __name__ == "__main__":
    x = ["flower", "flow", "flight"]
    x1 = longestCommonPrefix(x)
    print(x)
    print(x1)
    y = ["dog", "racecar", "car"]
    y1 = longestCommonPrefix(y)
    print(y)
    print(y1)

