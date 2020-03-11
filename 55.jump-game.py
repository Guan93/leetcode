#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    # top-down dp: O(n^2) and O(n)
    def canJump(self, nums: List[int]) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def _helper(i):
            if i == len(nums) - 1:
                return True

            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if _helper(j):
                    return True
            return False

        return _helper(0)

    # bottom-up dp: O(n^2) and O(n)
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in reversed(range(len(nums) - 1)):
            for j in range(i + 1, min(len(nums), i + nums[i])):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]

    # bottom-up dp (different direction): O(n^2) and O(n)
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            for j in reversed(range(i)):
                if dp[j] and i - j <= nums[j]:
                    dp[i] = True
                    break
        return dp[-1]

    # greedy: O(n) and O(1)
    def canJump(self, nums: List[int]) -> bool:
        reachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if reachable - i <= nums[i]:
                reachable = i
        return reachable == 0

# @lc code=end
