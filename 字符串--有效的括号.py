# -*- coding = utf-8 -*-
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        pare_lst = ["()", "{}", "[]"]
        right = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                right.append(s[i])
            else:
                if len(right) == 0:
                    return False
                elif right[-1] + s[i] in pare_lst:
                    right.pop()
                else:
                    return False
        if len(right) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    ans = sol.isValid("[])")
    print(ans)