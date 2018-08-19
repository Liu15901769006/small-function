# -*- coding = utf-8 -*-


def plusOne(digits):
    """
    :type digits: list
    :rtype:list
    """
    sum = 0
    for i in digits:
        sum = sum*10 + i
    return [int(x) for x in str(sum+1)]


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(nums)
    print(plusOne(nums))

    nums = [4, 3, 2, 1]
    print(nums)
    print(plusOne(nums))
