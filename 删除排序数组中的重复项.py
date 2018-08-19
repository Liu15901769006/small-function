# -*- coding = utf-8 -*-


def removeDuplicates(nums):
    """
    :type nums:list
    :rtype:int
    """
    if not nums:
        return 0
    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index = index + 1
            nums[index] = nums[i]
    return index + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    ans = removeDuplicates(nums)
    print(ans)
    print(nums[:ans])

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ans = removeDuplicates(nums)
    print(ans)
    print(nums[:ans])