# -*- coding = utf-8 -*-


def generateParenthesis(n):
    """
    :type n: int
    :rtype: list
    """
    def dfs(left, path, res, n):
        if len(path) == 2 * n:
            if left == 0:
                res.append("".join(path))
            return
        if left < n:
            path.append("(")
            dfs(left + 1, path, res, n)
            path.pop()
        if left > 0:
            path.append(")")
            dfs(left - 1, path, res, n)
            path.pop()
    res = []
    dfs(0, [], res, n)
    return res


if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))