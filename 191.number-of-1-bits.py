#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#


# @lc code=start
class Solution(object):
    def hammingWeight(self, n: int) -> int:
        mask = 1
        count = 0
        for i in range(32):
            if n & mask:
                count += 1
            mask = mask << 1
        return count


# @lc code=end
