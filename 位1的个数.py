# -*- coding = utf-8 -*-


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    r_string = ""
    x = n // 2
    y = n % 2
    r_string += str(y)
    while x != 0:
        y = x % 2
        r_string += str(y)
        x = x // 2
    bit_string = r_string[::-1]
    ans = 0
    for i in range(len(bit_string)):
        if int(bit_string[i]) == 1:
            ans += 1
    return ans


if __name__ == "__main__":
    n = 11
    ans = hammingWeight(n)
    print(ans)

    n = 128
    ans = hammingWeight(ans)
    print(ans)