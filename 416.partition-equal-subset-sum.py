#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#


# @lc code=start
class Solution:
    # dp 0/1 knapsack: O(ns) and O(ns)
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # return False if the sum is odd
        if s & 1:
            return False
        n = len(nums)
        target = int(s / 2)

        # dp[i][j]: from the first i numbers whether we can pick several whose sum is j
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # if we don't pick nums[i], dp[i][j] = dp[i - 1][j];
                # if we  pick nums[i], dp[i][j] = dp[i - 1][j - nums[i]];
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]

    # optimized space dp
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # return False if the sum is odd
        if s & 1:
            return False
        n = len(nums)
        target = int(s / 2)

        dp = [True] + [False] * (target)
        for i in range(1, n + 1):
            dp = [
                dp[j] or (j >= nums[i - 1] and dp[j - nums[i - 1]])
                for j in range(target + 1)
            ]
        return dp[target]

    # backtrack with pruning
    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def _helper(i, curr):
            if curr == target:
                return True

            for j in range(i + 1, len(nums)):
                # since nums are already sorted, we can prune impossible paths here
                if curr + nums[j] > target:
                    return False
                if _helper(j, curr + nums[j]):
                    return True
            return False

        target, rem = divmod(sum(nums), 2)
        if rem:
            return False
        nums.sort()

        return _helper(-1, 0)

# @lc code=end
