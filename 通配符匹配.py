# -*- coding = utf-8 -*-


def isMatch(s,  p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    i = 0
    j = 0
    lastMatchPos = 0
    lastStarPos = -1
    while i < len(s):
        if j < len(p) and p[j] in (s[i], "?"):
            i += 1
            j += 1
        elif j < len(p) and p[j] == "*":
            lastMatchPos = i
            lastStarPos = j
            j += 1
        elif lastStarPos > -1:
            i = lastMatchPos + 1
            lastMatchPos += 1
            j = lastStarPos + 1
        else:
            return False
    while j < len(p) and p[j] == "*":
        j += 1
    return j == len(p)


if __name__ == "__main__":
    s_p_lst = [["aa", "a"], ["aa", "*"], ["cb", "?a"], ["adceb", "*a*b"], ["acdcb", "a*c?b"]]
    for s_p in s_p_lst:
        s = s_p[0]
        p = s_p[1]
        ans = isMatch(s, p)
        print(ans)