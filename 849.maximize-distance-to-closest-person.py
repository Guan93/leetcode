#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#


# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        cur_zeros = max_zeros = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                cur_zeros += 1
                max_zeros = max(max_zeros, cur_zeros)
            elif seats[i] == 1:
                cur_zeros = 0
        return (max_zeros + 1) // 2


# @lc code=end
