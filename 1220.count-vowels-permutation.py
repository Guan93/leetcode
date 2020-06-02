#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#


# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0:
            return 0
        LARGE_INT = 10 ** 9 + 7
        can_follow = [[1, 2, 4], [0, 2], [1, 3], [2], [2, 3]]
        dp = [[0] * 5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(5):
                dp[i][j] = sum(dp[i - 1][k] for k in can_follow[j]) % LARGE_INT

        return sum(dp[-1]) % LARGE_INT


# @lc code=end
