#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
class Solution:
    # cumsum brute force: O(n^2) and O(n), tle
    def shortestSubarray(self, A: List[int], K: int) -> int:
        cumsum = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            cumsum[i] = cumsum[i - 1] + A[i - 1]

        min_len = float("inf")
        for end in range(1, len(A) + 1):
            for start in range(end):
                if cumsum[end] - cumsum[start] >= K:
                    min_len = min(min_len, end - start)

        return min_len if min_len < float("inf") else -1

    # monoqueue: O(n) and O(n)
    def shortestSubarray(self, A: List[int], K: int) -> int:
        from collections import deque

        cumsum = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            cumsum[i] = cumsum[i - 1] + A[i - 1]

        min_len = len(A) + 1
        monoq = deque()

        for i in range(len(cumsum)):
            while monoq and cumsum[monoq[-1]] >= cumsum[i]:
                monoq.pop()

            while monoq and cumsum[i] - cumsum[monoq[0]] >= K:
                min_len = min(min_len, i - monoq.popleft())

            monoq.append(i)

        return min_len if min_len <= len(A) else -1

# @lc code=end

