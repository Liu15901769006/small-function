# -*- coding = utf-8 -*-


def multipy(nums1, nums2):
    """
    :type nums1: str
    :type nums2: str
    :rtype: str
    """
    ans  = [0] * (len(nums1) + len(nums2))
    for i, n1 in enumerate(reversed(nums1)):
        for j, n2 in enumerate(reversed(nums2)):
            ans[i + j] += int(n1) * int(n2)
            ans[i + j + 1] += ans[i + j] // 10
            ans[i + j] %= 10
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return "".join(map(str, ans[::-1]))


if __name__ == "__main__":
    nums1 = "123"
    nums2 = "456"
    ans = multipy(nums1, nums2)
    print(ans)
