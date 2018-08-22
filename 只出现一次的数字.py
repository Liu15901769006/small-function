# -*- coding = utf-8 -*-


def singleNumber(nums):
    """
    :type nums:list
    :rtype:int
    """
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]


if __name__ == "__main__":
    nums = [2, 2, 1]
    ans = singleNumber(nums)
    print(ans)

    nums = [4, 1, 2, 1, 2]
    ans = singleNumber(nums)
    print(ans)
