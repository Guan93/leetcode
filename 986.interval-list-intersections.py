#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#


# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        res = []
        while p1 < len(A) and p2 < len(B):
            a1, a2, b1, b2 = A[p1][0], A[p1][1], B[p2][0], B[p2][1]
            if a1 <= b2 and a2 >= b1 or b1 <= a2 and b2 >= a1:
                res.append([max(a1, b1), min(a2, b2)])
            if a2 < b2:
                p1 += 1
            else:
                p2 += 1

        return res


# @lc code=end
