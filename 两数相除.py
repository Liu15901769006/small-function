# -*- coding = utf-8 -*-
# 左移一位，变成原来的2倍

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype:int
    """
    if divisor == 0:
        return 0x7fffffff
    sign = 1
    if dividend * divisor < 0:
        sign = -1
    ans = 0
    cnt = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    subsum = divisor
    while dividend >= divisor:
        while (subsum << 1) <= dividend:
            cnt <<= 1
            subsum <<= 1
        ans += cnt
        cnt = 1
        dividend -= subsum
        subsum = divisor
    return max(min(sign * ans, 0x7fffffff), -2147483648)


if __name__ == "__main__":
    dividend = 10
    divisor = 3
    ans = divide(dividend, divisor)
    print(ans)