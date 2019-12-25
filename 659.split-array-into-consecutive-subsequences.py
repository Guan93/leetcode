#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start

# greedy: O(n) and O(1)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        cur = cnt = 0
        p1 = p2 = p3 = 0
        c1 = c2 = c3 = 0

        i = 0
        while i < len(nums):
            pre, cur, cnt = cur, nums[i], 0
            p1, p2, p3 = c1, c2, c3
            while i < len(nums) and nums[i] == cur:
                cur = nums[i]
                i, cnt = i + 1, cnt + 1
            if cur != pre + 1:
                if p1 != 0 or p2 != 0:
                    return False
                c1, c2, c3 = cnt, 0, 0
            else:
                if cnt < p1 + p2:
                    return False
                c1 = max(0, cnt - (p1 + p2 + p3))
                c2 = p1
                c3 = cnt - c1 - c2
        return c1 == 0 and c2 == 0


# @lc code=end
