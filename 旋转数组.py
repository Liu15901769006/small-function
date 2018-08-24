# -*- coding = utf-8 -*-


def rotate(nums, k):
    """
    :type nums:list
    :type k:int
    :rtype:void do not return anything, modify nums in-place instead
    """
    if len(nums) == 0 or k == 0:
        return
    def reverse(start, end, s):
        while start < end:
            be = s[end]
            s[end] = s[start]
            s[start] = be
            start += 1
            end -= 1
    n = len(nums) - 1
    k = k % len(nums)
    reverse(0, n - k, nums)
    reverse(n - k + 1, n, nums)
    reverse(0, n, nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)

    nums = [-1, -100, 3, 99]
    k = 2
    rotate(nums, k)
    print(nums)
