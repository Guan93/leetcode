#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#


# @lc code=start

# # brute force: O(3^N) and O(3^N)
# class Solution:
#     def checkRecord(self, n: int) -> int:

#         def _helper(num_prev_L=0, exist_A=False, i=0):
#             if i == n:
#                 return 1
#             res = 0
#             # put L
#             res += _helper(False, exist_A, i + 1)
#             if num_prev_L < 2:
#                 res += _helper(num_prev_L + 1, exist_A, i + 1)
#             # put A
#             if not exist_A:
#                 res += _helper(0, True, i + 1)
#             return res

#         return _helper(0, False, 0) % (1e9 + 7)


# using recursive formulae and dp: O(N) and O(N)
class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7

        dp = [0] * ((n + 1) if n >= 3 else 4)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7

        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] % M + (M - dp[i - 4]) % M
        res = dp[n]

        for i in range(1, n + 1):
            res += (dp[i - 1] * dp[n - i]) % M

        return res % M


# @lc code=end
