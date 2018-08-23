# -*- coding = utf-8 -*-


def lengthOfLastWord(s):
    """
    :type s:str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    s = s.split()
    if len(s) > 0:
        return len(s[-1])
    return 0


if __name__ == "__main__":
    s = "hello world"
    ans = lengthOfLastWord(s)
    print(ans)
