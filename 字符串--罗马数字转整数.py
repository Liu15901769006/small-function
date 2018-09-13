# -*- coding = utf-8 -*-
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_lst = [1000, 500, 100, 50, 10, 5, 1]
        char_lst = ["M", "D", "C", "L", "X", "V", "I"]
        merge_dict = dict(zip(char_lst, num_lst))
        ans = 0
        for i in range(len(s) - 1):
            if merge_dict[s[i]] < merge_dict[s[i + 1]]:
                ans -= merge_dict[s[i]]
            else:
                ans += merge_dict[s[i]]
        ans += merge_dict[s[-1]]
        return ans



