#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List

# class QuickUnionUF:
#     def __init__(self, n: int) -> None:
#         self.count = 0
#         self._parent = list(range(n))

#     def find(self, p: int) -> int:
#         while p != self._parent[p]:
#             p = self._parent[p]
#         return p

#     def connected(self, p: int, q: int) -> bool:
#         return self.find(p) == self.find(q)

#     def union(self, p: int, q: int) -> None:
#         rootP = self.find(p)
#         rootQ = self.find(q)
#         if rootP == rootQ:
#             return
#         self._parent[rootQ] = rootP
#         self.count -= 1


# class Solution:
#     def overlap(self, a: List[int], b: List[int]) -> bool:
#         return a[0] <= b[1] and b[0] <= a[1]

#     def merge_nodes(self, cc: List[List[int]]) -> List[int]:
#         start, end = cc[0][0], cc[0][1]
#         for interval in cc:
#             start = min(start, interval[0])
#             end = max(end, interval[1])
#         return [start, end]

#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         n = len(intervals)
#         cc = dict()
#         uf = QuickUnionUF(n)
#         for i, interval_i in enumerate(intervals):
#             for j in range(i + 1, n):
#                 if self.overlap(interval_i, intervals[j]):
#                     uf.union(i, j)

#         for i in range(n):
#             root_i = uf.find(i)
#             if root_i in cc:
#                 cc[root_i].append(intervals[i])
#             else:
#                 cc[root_i] = [intervals[i]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by their start value
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        connected_components = []
        cc = intervals[0]
        for interval in intervals[1:]:
            if cc[1] >= interval[0]:
                cc[1] = max(cc[1], interval[1])
            else:
                connected_components.append(cc)
                cc = interval
        connected_components.append(cc)
        return connected_components

#         # all intervals in each connected component must be merged.
#         return [self.merge_nodes(v) for k, v in cc.items()]


# @lc code=end
