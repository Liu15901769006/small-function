# -*- coding = utf-8 -*-


def combinationSum(candidates, target):
    """
    :type candidates: list
    :type target:int
    :rtype: list
    """
    def dfs(candidates, start, target, path, res):
        if target == 0:
            return res.append(path + [])
        for i in range(start, len(candidates)):
            if target - candidates[i] >= 0:
                path.append(candidates[i])
                dfs(candidates, i, target - candidates[i], path, res)
                path.pop()
    res = []
    dfs(candidates, 0, target, [], res)
    return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    ans = combinationSum(candidates, target)
    print(ans)

    candidates = [2, 3, 5]
    target = 8
    ans = combinationSum(candidates, target)
    print(ans)

