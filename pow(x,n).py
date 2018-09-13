# -*- coding = utf-8 -*-


def myPow(x, n):
    """
    :type x:float
    :type n:int
    :rtype:float
    """
    if n < 0:
        n = -n
        x = 1 / x
    ans = 1
    # while n:
    #     if n & 1:
    #         ans *= x
    #     x *= x
    #     n >>= 1
    # return ans
    while n:
        ans *= x
        n -= 1
    return ans


if __name__ == "__main__":
    nums = [[2.00000, 10], [2.10000, 3], [2.00000, -2]]
    for num in nums:
        ans = myPow(num[0], num[1])
        print(ans)