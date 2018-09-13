# -*- coding = utf-8 -*-
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]
        dp[0] = [1] * m
        for i in dp:
            i[0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        ans = dp[-1][-1]
        return ans


if __name__ == "__main__":
    m = 7
    n = 3
    s = Solution()
    ans = s.uniquePaths(m, n)
    print(ans)
    print("right answer = " + str(28))

