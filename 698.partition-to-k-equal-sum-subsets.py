#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#


# @lc code=start
class Solution:
    # # backtrack
    # def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    #     def _helper(visited, start_idx, k, cursum):
    #         if k == 1:
    #             return True
    #         if cursum == target:
    #             return _helper(visited, 0, k - 1, 0)
    #         if cursum > target:
    #             return False
    #         for i in range(start_idx, len(nums)):
    #             if not visited[i]:
    #                 visited[i] = True
    #                 if _helper(visited, i + 1, k, cursum + nums[i]):
    #                     return True
    #                 visited[i] = False
    #         return False

    #     target, r = divmod(sum(nums), k)
    #     if r != 0:
    #         return False
    #     visited = [False] * len(nums)
    #     return _helper(visited, 0, k, 0)

    # improve with memo
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def _helper(visited, start_idx, k, cursum):
            if k == 1:
                return True
            if cursum == target:
                return _helper(visited, 0, k - 1, 0)
            if cursum > target:
                return False
            for i in range(start_idx, len(nums)):
                mask = 1 << i
                if not visited & mask:
                    visited |= mask
                    if _helper(visited, i + 1, k, cursum + nums[i]):
                        return True
                    visited &= ~mask
            return False

        target, r = divmod(sum(nums), k)
        if r != 0:
            return False
        visited = 0
        return _helper(visited, 0, k, 0)


# @lc code=end
