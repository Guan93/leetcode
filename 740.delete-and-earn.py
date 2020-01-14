#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter

        counts = Counter(nums)
        prev_num = -1
        prev_points2 = prev_points1 = 0
        for num in sorted(counts.keys()):
            if prev_num + 1 == num:
                prev_points2, prev_points1 = prev_points1, max(prev_points1, prev_points2 + counts[num] * num)
            else:
                prev_points2, prev_points1 = prev_points1, prev_points1 + counts[num] * num
            prev_num = num
        return prev_points1


# @lc code=end

