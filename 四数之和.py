# -*- coding = utf-8 -*-


def fourSum(nums, target):
    """
    :type nums: list
    :type target: int
    :rtype: list
    """
    nums.sort()
    res = []
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            start = j + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[j] + nums[start] + nums[end]
                if sum < target:
                    start += 1
                elif sum > target:
                    end -= 1
                else:
                    res.append([nums[i], nums[j], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
    return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = fourSum(nums, target)
    print(ans)