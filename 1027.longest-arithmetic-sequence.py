#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
class Solution:
    # bottom up: O(mn) and O(mn)
    def longestArithSeqLength(self, A: List[int]) -> int:
        max_length = 0
        dp = [dict() for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                step = A[i] - A[j]
                length = dp[j].get(step, 1)
                dp[i][step] = length + 1
                max_length = max(dp[i][step], max_length)
        return max_length


# @lc code=end

