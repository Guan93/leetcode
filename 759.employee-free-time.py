"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    # making use of the solution in #56. merge-intervals
    # O(nlogn) and O(n) where n is the total number of merged intervals
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for s in schedule:
            for interval in s:
                intervals.append((interval.start, interval.end))

        intervals.sort()
        merged_intervals = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(intervals[j][1], end)
                j += 1
            merged_intervals.append((start, end))
            i = j

        return [
            Interval(first.end, second.start)
            for first, second in zip(merged_intervals[:-1], merged_intervals[1:])
        ]

    # construct results in one go
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res

    # same idea as previous solution, but making use of the fact that schedule for each
    # worker is already sorted, therefore we can use priority queue to improve time complexity.
    # similar to #23.merge-k-sorted-lists
    # O(nlogk) and O(n)
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        import heapq

        pq, res = [], []
        for i, worker in enumerate(schedule):
            heapq.heappush(pq, ((worker[0].start, worker[0].end), i, 0))

        prev_end = -1
        while pq:
            (start, end), i, j = heapq.heappop(pq)
            j += 1
            if j < len(schedule[i]):
                heapq.heappush(pq, ((schedule[i][j].start, schedule[i][j].end), i, j))
            if prev_end < start:
                res.append(Interval(prev_end, start))
            prev_end = max(prev_end, end)

        return res[1:]
