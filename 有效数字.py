# -*- coding = utf-8 -*-


def isNum(s):
    """
    :type s:str
    :rtype:bool
    """
    sign = "0123456789"
    for i, element in enumerate(s):
        if element not in sign:
            if element == "-" and i == 0:
                continue
            elif element == "." and i > 0:
                continue
            else:
                return False
    return True


if __name__ == "__main__":
    nums = ["0", "0.1", "abc", "1 a", "2e10"]
    for s in nums:
        ans = isNum(s)
        print(s, ans)
