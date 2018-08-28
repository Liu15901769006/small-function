# -*- coding = utf-8 -*-


def permute(nums):
    """
    :type nums: list
    :rtype: list
    """
    res = []
    visited = set([])
    def dfs(nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path + [])
            return
        for i in range(0, len(nums)):
            if i not in visited:
                visited.add(i)
                path.append(nums[i])
                dfs(nums, path, res, visited)
                path.pop()
                visited.discard(i)
    dfs(nums, [], res, visited)
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    ans = permute(nums)
    print(ans)