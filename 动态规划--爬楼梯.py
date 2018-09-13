# -*- coding = utf-8 -*-
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        dp[0] = 1
        dp[1] = 2
        dp[2] = 3
        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        ans = dp[-1]
        return ans