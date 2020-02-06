#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        single_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        double_dict = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}

        num = i = 0
        while i < len(s):
            if s[i] in double_dict and i < len(s) - 1 and s[i + 1] in double_dict[s[i]]:
                num += single_dict[s[i + 1]] - single_dict[s[i]]
                i += 2
            else:
                num += single_dict[s[i]]
                i += 1
        return num
# @lc code=end

