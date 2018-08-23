# -*- coding = utf-8 -*-


def romanToInt(s):
    """
    :type s:str
    :rtype:int
    """
    d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    ans = 0
    for i in range(0, len(s) - 1):
        c = s[i]
        cafter = s[i + 1]
        if d[c] < d[cafter]:
            ans -= d[c]
        else:
            ans += d[c]
    ans += d[s[-1]]

    return ans


if __name__ == "__main__":
    s1 = "III"
    ans = romanToInt(s1)
    print(ans)

    s2 = "IV"
    ans = romanToInt(s2)
    print(ans)

    s3 = "IX"
    ans = romanToInt(s3)
    print(ans)

    s4 = "LVIII"
    ans = romanToInt(s4)
    print(ans)

    s5 = "MCMXCIV"
    ans = romanToInt(s5)
    print(ans)

