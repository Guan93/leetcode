#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                end = nums[i]
            else:
                res.append(f'{start}->{end}')
                start, end = nums[i], None
        res.append(f'{start}->{end}' if end is not None else str(start))
        return res


# @lc code=end
