#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing_ranges = []
        nums.append(upper + 1)
        prev = lower - 1
        for num in nums:
            if num == prev + 2:
                missing_ranges.append(f"{num - 1}")
            elif num > prev + 2:
                missing_ranges.append(f"{prev + 1}->{num - 1}")
            prev = num
        return missing_ranges


# @lc code=end
