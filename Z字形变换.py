# -*-coding = utf-8-*-


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    ff = []
    j = -1
    s = list(s)
    for i in range(numRows):
        ff.append([])
    while s != []:
        while j < numRows -1 and s != []:
            j += 1
            ff[j].append(s.pop(0))
        while j > 0 and s != []:
            j -= 1
            ff[j].append(s.pop(0))

    s = ''
    for i in range(numRows):
        s = s + ''.join(ff[i])
    return s


if __name__ == "__main__":
    s = 'PAYPALISHIRING'
    numRows = 4
    ans = convert(s, numRows)
    print(ans)