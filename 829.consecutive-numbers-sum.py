#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#


# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        K = int(((2 * N) + 0.25)**0.5 - 0.5)
        res = 0
        for k in range(1, K + 1):
            if ((N - k * (k + 1) / 2) % k == 0):
                res += 1
        return res


# @lc code=end
