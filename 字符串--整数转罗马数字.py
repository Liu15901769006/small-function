# -*- coding = utf-8 -*-
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_lst = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        char_lst = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ""
        if num > 3999 or num < 1:
            return ""
        for i in range(len(num_lst)):
            while num >= num_lst[i]:
                ans += char_lst[i]
                num -= num_lst[i]
        return ans

