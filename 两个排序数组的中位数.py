# -*- coding = utf-8 -*-


def findMedianSortedArrays(num1, num2):
    """
    :type num1: List
    :type num2: List
    :rtype: float
    """
    length1 = len(num1)
    length2 = len(num2)
    total = length1 + length2
    print(total)

    alist = []
    while len(num1) and len(num2):
        if num1[0] < num2 [0]:
            alist.append(num1.pop(0))
        else:
            alist.append(num2.pop(0))
    if len(num2) == 0:
        alist += num1
    if len(num1) == 0:
        alist += num2
    print(alist)

    if total % 2 == 0:
        half = int(total / 2)
        return (alist[half] + alist[half - 1]) / 2
    else:
        half = int(total / 2)
        return alist[half]


if __name__ == "__main__":
    num1 = [1, 2]
    num2 = [3, 4]
    half = findMedianSortedArrays(num1, num2)
    print(half)
