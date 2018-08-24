# -*- coding = utf-8 -*-
# 十进制整数转换为二进制整数采用除2取余， 逆序排列


def reverseBits(n):
    """
    :type n:int
    :rtype:int
    """
    r_string = ""
    x = n // 2
    y = n % 2
    r_string += str(y)
    while x != 0:
        y = x % 2
        r_string += str(y)
        x = x // 2
    bit_string =  r_string[::-1]
    diff = "0" * (32 - len(bit_string))
    bit_string = diff + bit_string
    string = bit_string[::1]
    ans = 0
    for i in range(len(string)):
        ans += int(string[i]) * 2 ** (i)
    return ans


if __name__ == "__main__":
    n = 43261596
    ans = reverseBits(n)
    print(n)
    print(ans)
