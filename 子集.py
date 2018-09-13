# -*- coding = utf-8 -*-


def subsets(nums):
    """
    :type nums:list
    :rtype:list
    """
    def dfs(nums, index, path, ans):
        ans.append(path)
        [dfs(nums, i + 1, path + [nums[i]], ans) for i in range(index, len(nums))]
    ans = []
    dfs(nums, 0, [], ans)
    return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    ans = subsets(nums)
    print(ans)

