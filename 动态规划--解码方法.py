# -*- coding = utf-8 -*-
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if int(s[i - 1: i + 1]) == 10 or int(s[i - 1:i + 1]) == 20:
                dp[i] = dp[i - 1]
            elif int(s[i - 1: i + 1]) > 10 and int(s[i - 1:i + 1]) <= 26:
                dp[i] = dp[i - 1] + 1
            elif int(s[i]) != 0:
                dp[i] = dp[i - 1]
            else:
                return 0
        ans = dp[-1]
        return ans

if __name__ == "__main__":
    s = "101"
    T = Solution()
    ans = T.numDecodings(s)
    print(ans)