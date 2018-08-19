# -*- coding = utf-8 -*-


def isPalindrome(x):
    """
    :type x: int
    :rtype:bool
    """
    s = list(str(x))
    s1 = list(str(x))
    s1.reverse()
    if s1 == s:
        return True
    else:
        return False


if __name__ == "__main__":
    x = 121
    ans = isPalindrome(x)
    print(ans)
    y = -11
    print(isPalindrome(y))
    