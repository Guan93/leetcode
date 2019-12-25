#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     self.dfs(nums, 0, [], res)
    #     return res

    # def dfs(self, nums: List[int], index: int, path: List[int],
    #         res: List[List[int]]) -> None:
    #     res.append(path)
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            to_add = []
            for res in results:
                to_add.append(res + [num])
            results += to_add
            # results += [res + [num] for res in results]
        return results


# @lc code=end
