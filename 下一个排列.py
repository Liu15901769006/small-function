# -*- coding = utf-8 -*-


def reverse(nums, start, end):
    while start < end:
        be = nums[start]
        nums[start] = nums[end]
        nums[end] = be
        start += 1
        end -= 1

def nextPermutation(nums):
    """
    :type nums:list
    :rtype:void do not return anything, modify nums in-place instead
    """
    if nums is None or len(nums) <= 1:
        return
    pos = None
    p = len(nums) - 2
    # find the first number that is not in correct order
    while p >= 0:
        if nums[p + 1] > nums[p]:
            pos = p
            break
        p -= 1
    if pos is None:
        reverse(nums, 0, len(nums) - 1)
        return

    # find the min value in the rest of the array
    minPos = pos + 1
    minV = nums[pos + 1]
    for i in range(pos + 1, len(nums)):
        if nums[i] < minV and nums[i] > nums[pos]:
            minV = nums[i]
            minPos = i
    # swap the two above number and reverse the array from "pos"
    be = nums[pos]
    nums[pos] = nums[minPos]
    nums[minPos] = be
    reverse(nums, pos + 1, len(nums) - 1)


if __name__ == "__main__":
    nums = [[1, 2, 3], [3, 2, 1], [1, 1, 5]]
    for num in nums:
        print(num)
        nextPermutation(num)
        print(num)



