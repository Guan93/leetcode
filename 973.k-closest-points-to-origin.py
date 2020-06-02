#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq

        pq = []
        for x, y in points:
            heapq.heappush(pq, (- x * x - y * y, x, y))
            if len(pq) > K:
                heapq.heappop(pq)

        return [[x, y] for _, x, y in pq]

# @lc code=end

