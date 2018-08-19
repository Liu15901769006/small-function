# -*- coding = utf-8 -*-


def maxSubArray(nums):
    """
    :type nums:list
    :rtype:int
    """
    maxSum = nums[0]
    curSum = nums[0]
    for i in range(1, len(nums)):
        curSum = max(nums[i], curSum + nums[i])
        maxSum = max(curSum, maxSum)
    return maxSum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans =maxSubArray(nums)
    print(ans)
