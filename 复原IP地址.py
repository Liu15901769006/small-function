# -*- coding = utf-8 -*-


def restoreIpAddresses(s):
    """
    :type s: str
    :rtype:list
    """
    ans = []
    n = len(s)
    def isvalid(num):
        if len(num) == 1:
            return True
        if len(num) > 1 and num[0] != "0" and int(num) <= 255:
            return True
        return False

    for i in range(0, min(3, n - 3)):
        a = s[:i + 1]
        if not isvalid(a):
            continue
        for j in range(i + 1, min(i + 4, n - 2)):
            b = s[i + 1:j + 1]
            if not isvalid(b):
                continue
            for k in range(j + 1, min(j + 4, n - 1)):
                c = s[j + 1:k + 1]
                d = s[k + 1:]
                if not isvalid(c):
                    continue
                if not isvalid(d):
                    continue
                ans.append("{}.{}.{}.{}".format(a, b, c, d))
    return ans


if __name__ == "__main__":
    s = "25525511135"
    ans = restoreIpAddresses(s)
    print(ans)

