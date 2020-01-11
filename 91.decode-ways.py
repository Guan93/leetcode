#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 0, 1
        prev_num = 0

        for i in range(0, len(s)):
            curr_num = int(s[i])
            curr = ((prev1 if curr_num > 0 else 0) +
                    (prev2 if 10 <= prev_num * 10 + curr_num <= 26 else 0))
            prev2, prev1 = prev1, curr
            prev_num = curr_num
        return prev1


# @lc code=end
