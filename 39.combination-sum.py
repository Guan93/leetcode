#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self._dfs(candidates, target, 0, [], res)
        return res

    def _dfs(self, nums: List[int], target: int, index: int, path: List[int],
             res: List[List[int]]) -> None:
        # if target < 0:
        #     return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if target < nums[i]:
                break
            self._dfs(nums, target - nums[i], i, path + [nums[i]], res)


# @lc code=end
