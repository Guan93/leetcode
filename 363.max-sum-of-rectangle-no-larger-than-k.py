#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#


# @lc code=start
# dp: O(m^2 n^2) and O(mn) (TLE)
class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        res = -1000000000
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][
                    j - 1]
                for x in range(i):
                    for y in range(j):
                        area = dp[i][j] - dp[x][j] - dp[i][y] + dp[x][y]
                        if area <= k:
                            res = max(area, res)
        return res


# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596/Any-Accepted-Python-Solution
# python does not have built-in ordered set/dict, making it hard to achieve complexity better
# than O(m^2 n^2)
class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], target: int) -> int:
        import heapq

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = -1000000000
        for i in range(1, m + 1):
            cumsum = [0] * n
            for j in reversed(range(i)):
                sum_row = 0
                heap = []
                heapq.heappush(heap, 0)
                for k in range(n):
                    cumsum[k] += matrix[j][k]
                    sum_row += cumsum[k]
                    idx = self.bisect_heap(heap, sum_row - target)
                    if idx < len(heap):
                        res = max(res, sum_row - heapq.nsmallest(idx, heap)[-1])
                    heapq.heappush(heap, sum_row)
        return res

    def bisect_heap(self, heap, target):
        lo, hi = 0, len(heap)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if heapq.nsmallest(mid, heap)[-1] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


# @lc code=end
