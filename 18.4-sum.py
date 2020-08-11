#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc code=start
# Time: O(n^(k-1)) if k > 2 else O(nlogn)
# Space: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.KSum(nums, 0, target, 4)

    def KSum(self, nums, start_idx, target, k):
        res = []
        if start_idx >= len(nums) or nums[start_idx] * k > target or nums[-1] * k < target:
            return res
        if k == 2:
            return self.twoSum(nums[start_idx:], target)

        for i in range(start_idx, len(nums)):
            if i != start_idx and nums[i - 1] == nums[i]:
                continue
            res.extend([[nums[i]] + set_
                        for set_ in self.KSum(nums, i + 1, target - nums[i], k - 1)])
        return res

    def twoSum(self, nums, target):
        res = []
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target or (lo > 0 and nums[lo - 1] == nums[lo]):
                lo += 1
            elif s > target or (hi < len(nums) - 1 and nums[hi + 1] == nums[hi]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
        return res


# @lc code=end
