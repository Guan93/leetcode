#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#

# @lc code=start
import collections

# # sort by column O(n^2) and O(n^2)
# class Solution:
#     def minAreaRect(self, points: List[List[int]]) -> int:
#         columns = collections.defaultdict(list)
#         for x, y in points:
#             columns[x].append(y)
#         lastx = dict()

#         ans = float("inf")
#         for x in sorted(columns):
#             column = columns[x]
#             column.sort()
#             for j, y2 in enumerate(column):
#                 for i in range(j):
#                     y1 = column[i]
#                     if (y1, y2) in lastx:
#                         ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
#                     lastx[y1, y2] = x
#         return ans if ans < float("inf") else 0


# count by diagonal O(n^2) and O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        ans = float("inf")

        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S
                        and (p2[0], p1[1]) in S):
                    ans = min(ans, abs((p2[0] - p1[0]) * (p2[1] - p1[1])))
        return ans if ans < float("inf") else 0


# @lc code=end
