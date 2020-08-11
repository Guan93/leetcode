#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
# O(n^2) TLE
class Solution1:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


# bfs: O(n) and O(1)
class Solution2:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        level = curr_max = next_max = i = 0
        while curr_max - i + 1 > 0:  # num of nodes in current level
            level += 1  # next level
            while i <= curr_max:
                next_max = max(next_max, i + nums[i])
                if next_max >= n - 1:
                    return level
                i += 1
            curr_max = next_max
        return 0


# @lc code=end
