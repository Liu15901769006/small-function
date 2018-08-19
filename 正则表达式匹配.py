# -*- coding = utf-8 -*-


def isMatch(s, p):
    """
    :type s:str
    :type p: str
    :rtype:bool
    """
    slen = len(s)
    plen = len(p)
    if plen == 0:
        return slen == 0
    if plen == 1:
        if (p == s) or ((p == '.') and (len(s) == 1)):
            return True
        else:
            return False
    if (p[-1] != '*') and (p[-1] != ".") and (p[-1] not in s):
        return False
    if (p[1] != "*"):
        if (len(s) > 0) and ((p[0] == s[0]) or (p[0] == ".")):
            return isMatch(s[1:], p[1:])
        return False
    else:
        while(len(s) > 0) and ((p[0] == s[0]) or (p[0] == ".")):
            if(isMatch(s, p[2:])):
                return True
            s = s[1:]
        return isMatch(s, p[2:])