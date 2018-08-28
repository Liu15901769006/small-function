# -*- coding = utf-8 -*-


def combinationSum2(candidates, target):
    """
    :type candidates: list
    :type target: int
    :rtype: list
    """
    def dfs(nums, target, start, visited, path, res):
        if target == 0:
            res.append(path + [])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if target - nums[i] < 0:
                return 0
            if i not in visited:
                visited.add(i)
                path.append(nums[i])
                dfs(nums, target - nums[i], i + 1, visited, path, res)
                path.pop()
                visited.discard(i)
    candidates.sort()
    res = []
    visited = set([])
    dfs(candidates, target, 0, visited, [], res)
    return res


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = combinationSum2(candidates, target)
    print(ans)
