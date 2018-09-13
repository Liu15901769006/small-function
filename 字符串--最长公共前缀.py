# -*- coding = utf-8 -*-
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = []
        n = len(strs)
        minLen = min(len(s) for s in strs)
        for index in range(minLen):
            tmp = []
            for i in range(n):
                tmp.append(strs[i][index])
            if len(set(tmp)) == 1:
                ans.append(tmp[0])
            else:
                break
        result = "".join(ans)
        return result