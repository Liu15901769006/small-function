# -*- coding = utf-8 -*-


def reverse(x):
    """
    :type x:int
    :rtype:int
    """
    if x < -pow(2, 31) or x > pow(2, 31)-1:
        return 0
    s = str(x)
    if len(s) == 1:
        return x
    s = s[::-1]
    if s.startswith("0"):
        s = s.lstrip("0")
    if s.endswith("-"):
        s = '-' + s.rstrip("-")
    i = int(s)
    if i < -pow(2, 31) or i > pow(2, 31)-1:
        return 0
    return i


if __name__ == "__main__":
    x = 130
    print(x)
    x1 = reverse(x)
    print(x1)
    y = -130
    print(y)
    y2 = reverse(y)
    print(y2)
