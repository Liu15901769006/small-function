# -*- coding = utf-8 -*-


def twoSum(nums, target):
    """
    :type nums: List
    :type target: int
    :rtype: List
    """
    for i in nums:
        if i+1 < len(nums):
            for j in nums[i+1:]:
                if i + j == target:
                    return [nums[i].index, nums[j].index]

    print("there are not suitable digitals !")

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target)