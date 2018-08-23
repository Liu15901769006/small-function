# -*- coding = utf-8 -*-


def isValid(s):
    """
    :type s: str
    :rtype:bool
    """
    stack = []
    d = ["()", "[]", "{}"]
    for i in range(0, len(s)):
        stack.append(s[i])
        if (len(stack) >= 2) and (stack[-2] + stack[-1] in d) :
            stack.pop()
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))
    print(isValid(s4))
    print(isValid(s5))
