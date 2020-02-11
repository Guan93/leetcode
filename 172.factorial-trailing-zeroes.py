#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

    def trailingZeroes(self, n):
        count = 0
        while n:
            n = n // 5
            count += n
        return count

# @lc code=end

