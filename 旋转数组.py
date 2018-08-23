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
            s[]