# -*- coding = utf-8 -*-


def firstMissingPositive(nums):
    """
    :type nums:list
    :rtype:int
    """
    i = 0
    while i < len(nums):
        if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
            be = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = be
        else:
            i += 1

    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


if __name__ == "__main__":
    nums = [-1, -1, -1]
    ans = firstMissingPositive(nums)
    print(ans)

