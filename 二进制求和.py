# -*- coding = utf-8 -*-


def addBinary(a, b):
    """
    :type a:str
    :type b: str
    :rtype:str
    """
    diff = abs(len(a) - len(b))
    if len(a) > len(b):
        b = "0" * diff + b
    else:
        a = "0" * diff + a

    ret = ""
    carry = 0
    ai = len(a) - 1
    bi = len(b) - 1

    while ai >= 0 and bi >= 0:
        ac =a[ai]
        bc = b[bi]
        if ac == "1" and bc == "1":
            if carry == 1:
                ret += "1"
            else:
                ret += "0"
            carry = 1
        elif ac == "0" and bc == "0":
            if carry == 1:
                ret += "1"
            else:
                ret += "0"
            carry = 0
        else:
            if carry == 1:
                ret += "0"
            else:
                ret += "1"
        ai -= 1
        bi -= 1
    if carry == 1:
        ret += "1"
    return ret[::-1]


if __name__ == "__main__":
    a = "11"
    b = "1"
    ans = addBinary(a, b)
    print(ans)

    a = "1010"
    b = "1011"
    ans = addBinary(a, b)
    print(ans)