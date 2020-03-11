#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start


class Solution:
    # two pointers: O(nlogn) and O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
        return res

# @lc code=end
