#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq


class Solution:
    # # binary search: O(mn * log(max_ele - min_ele)) and O(1)
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     lo, hi = matrix[0][0], matrix[m - 1][n - 1] + 1
    #     while lo < hi:
    #         mid = lo + (hi - lo) // 2
    #         count, j = 0, m
    #         for i in range(m):
    #             while j > 0 and matrix[i][j - 1] > mid:
    #                 j -= 1
    #             count += j
    #         if count < k:
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return lo

    # heap: O(mn * logk) and O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pq = []
        for i in range(min(k, m)):
            heapq.heappush(pq, (matrix[i][0], i, 0))  # (num, row, col)
        
        count = 0
        while pq:
            num, row, col = heapq.heappop(pq)
            count += 1
            if count == k:
                break
            if col < n - 1:
                heapq.heappush(pq, (matrix[row][col + 1], row, col + 1))
        return num
# @lc code=end

