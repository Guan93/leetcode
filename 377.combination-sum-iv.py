#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        from functools import lru_cache

        @lru_cache(None)
        def _dfs(target: int):
            count = 0
            if target == 0:
                return count + 1

            for num in nums:
                if target < num:
                    break
                count += _dfs(target - num)
            return count
        return _dfs(target)

# @lc code=end

