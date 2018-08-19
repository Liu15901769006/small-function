# -*- coding = utf-8 -*-


def removeElement(nums, val):
    """
    :type nums:list
    :type val:int
    :rtype:int
    """
    index = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index = index + 1
    return index


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    ans = removeElement(nums, val)
    print(ans)
    print(nums[:ans])

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    ans = removeElement(nums, val)
    print(ans)
    print(nums[:ans])

