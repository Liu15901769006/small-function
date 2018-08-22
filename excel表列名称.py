# -*- coding = utf-8 -*-


def convertToTitle(n):
    """
    :type n:int
    :rtype:str
    """
    ans = ""
    if n <= 26:
        ans = chr(ord("A") + n -1)
    else:
        y = n // 26
        ans += chr(ord("A") + y - 1)
        x = n % 26
        ans += chr(ord("A") + x - 1)
    return ans


if __name__ == "__main__":
    nums = [1, 28, 701]
    for n in nums:
        ans = convertToTitle(n)
        print(ans)
