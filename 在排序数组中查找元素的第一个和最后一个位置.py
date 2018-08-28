# -*- coding = utf-8 -*-


def searchRange(nums, target):
    """
    :type nums: list
    :type target: int
    :rtype:list
    """
    l = 0
    r = len(nums) - 1
    found = 0
    start = 0
    end = 0
    while l < r:
        m = l + int((r - l) / 2)
        if target > nums[m]:
            l = m + 1
        else:
            if target == nums[m]:
                found += 1
            r = m - 1
    if nums[l] == target:
        found += 1

    start = r
    if nums[r] != target or r < 0:
        start = r + 1
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + int((r - l) / 2)
        if target < nums[m]:
            r = m - 1
        else:
            if target == nums[m]:
                found += 1
            l = m + 1
    end = l
    if nums[l] != target:
        end = l - 1

    if found == 0:
        return [-1, -1]

    return [start, end]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    ans = searchRange(nums, target)
    print(ans)