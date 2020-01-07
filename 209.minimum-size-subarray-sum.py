#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    # # binary search: O(nlogn) and O(n)
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     cumsum = [0]
    #     for num in nums:
    #         cumsum.append(cumsum[-1] + num)

    #     lo, hi = 0, len(nums) + 1
    #     while lo < hi:
    #         mid = lo + (hi - lo) // 2
    #         max_sum = max([cumsum[i + mid] - cumsum[i] for i in range(len(cumsum) - mid)])
    #         if max_sum < s:
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return lo if lo < len(nums) + 1 else 0

    # two pointers: O(n) and O(1)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = len(nums) + 1
        left = sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            while sum_ >= s and left <= i:
                res = min(res, i + 1 - left)
                sum_ -= nums[left]
                left += 1
        return res if res < len(nums) + 1 else 0

# @lc code=end
