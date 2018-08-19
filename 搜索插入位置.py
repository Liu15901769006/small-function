# -*- coding = utf-8 -*-


def searchInsert(nums, target):
    """
    :type nums:list
    :type target:int
    :rtype:int
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((right - left) / 2 + left)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    val =5
    ans = searchInsert(nums, val)
    print(ans)

    nums = [1, 3, 5, 6]
    val = 2
    ans = searchInsert(nums, val)
    print(ans)

    nums = [1, 3, 5, 6]
    val = 7
    ans = searchInsert(nums, val)
    print(ans)

    nums = [1, 3, 5, 6]
    val = 0
    ans = searchInsert(nums, val)
    print(ans)
    