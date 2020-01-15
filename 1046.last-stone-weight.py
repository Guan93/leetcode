#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    # O(nlogn) and O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        pq = []
        for w in stones:
            heapq.heappush(pq, -w)

        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x < y:
                heapq.heappush(pq, x - y)

        return -pq[0] if len(pq) > 0 else 0


# @lc code=end

