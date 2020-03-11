#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc code=start
#
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not p:
#             return not s

#         first_match = bool(s) and p[0] in {s[0], '.'}
#         if len(p) >= 2 and p[1] == '*':
#             # when encountered '*', we can either skip the first char in the pattern
#             # i.e., match zero first chars or match it
#             return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
#         else:
#             return first_match and self.isMatch(s[1:], p[1:])


# # top-down dp: O(sp) and O(sp)
# from functools import lru_cache


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         @lru_cache(None)
#         def dp(i, j):
#             if j == len(p):
#                 return i == len(s)

#             first_match = i < len(s) and p[j] in {s[i], '.'}
#             if len(p) - j >= 2 and p[j + 1] == '*':
#                 return dp(i, j + 2) or first_match and dp(i + 1, j)
#             else:
#                 return first_match and dp(i + 1, j + 1)
#         return dp(0, 0)


# bottom-up dp: O(sp) and O(sp)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for i in reversed(range(len(s) + 1)):
            for j in reversed(range(len(p))):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if len(p) - j >= 2 and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    # from left to right
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or i > 0 and p[j - 2] in (s[i - 1], '.') and dp[i - 1][j]
                else:
                    dp[i][j] = i > 0 and p[j - 1] in (s[i - 1], '.') and dp[i - 1][j - 1]

        return dp[m][n]

    # O(sp) and O(p)
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
        curr[0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 2] or i > 0 and p[j - 2] in (s[i - 1], '.') and prev[j]
                else:
                    curr[j] = i > 0 and p[j - 1] in (s[i - 1], '.') and prev[j - 1]
            for j in range(n + 1):
                prev[j] = curr[j]
                curr[j] = False
        return prev[-1]


# @lc code=end
