# -*- coding = utf-8 -*-


def merge(nums1, m, nums2, n):
    """
    :type nums1: list
    :type m: int
    :type nums2: list
    :type n:int
    :rtype: void do not return anything, modify nums1 in-place instead
    """
    while m > 0 and n > 0:
        if nums1[m -1] > nums2[n - 1]:
            nums1[m + n -1] = nums1[m - 1]
            m = m - 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    print(nums1)
    m = 3
    nums2 = [2, 5, 6]
    print(nums2)
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
