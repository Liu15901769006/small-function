# -*- coding = utf-8 -*-
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_lst = ["2", "3", "4", "5", "6", "7", "8", "9"]
        char_lst = [["a", "b", "c"], ["d", "e", "f"], ["g", "h","i"], ["j", "k", "l"], ["m", "n", "o"],
                    ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        merge_dict = dict(zip(num_lst, char_lst))
        ans = []
        for i in range(len(digits)):
            if len(ans) == 0:
                ans.extend(merge_dict[digits[i]])
            else:
                tmp = []
                for a in ans:
                    for j in merge_dict[digits[i]]:
                        tmp.append(a + j)
                ans = tmp
        return ans


