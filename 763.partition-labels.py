#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lc code=start
# make use of #56 merge-intervals
class Solution1:
    def partitionLabels(self, S: str) -> List[int]:
        intervals = dict()
        for i, c in enumerate(S):
            if c not in intervals:
                intervals[c] = [i, i]
            else:
                intervals[c][1] = i
        merged_intervals = self.merge(intervals.values())
        return [interval[1] - interval[0] + 1 for interval in merged_intervals]

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


class Solution2:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []
        for i, c in enumerate(S):
            end = max(last[c], end)
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1
        return res

# @lc code=end
