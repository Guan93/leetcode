#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#


# @lc code=start

# # 1. dp to store start indexes
# # dp[i] means the start index of the possible longest valid string ending at i
# # for invalid ')' at index i, dp[i] = -1
# # O(n) and O(n)
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) <= 1:
#             return 0
#         global_max = 0
#         dp = [-1] * len(s)
#         dp[0] = 0 if s[0] == '(' else -1
#         for i in range(1, len(s)):
#             if s[i] == ')':
#                 # "()"
#                 if s[i - 1] == '(':
#                     dp[i] = dp[i - 1]
#                     global_max = max(global_max, i - dp[i] + 1)
#                 # "))"
#                 elif dp[i - 1] > 0 and s[dp[i - 1] - 1] == '(':
#                     dp[i] = dp[dp[i - 1] - 1]
#                     global_max = max(global_max, i - dp[i] + 1)
#             else:
#                 # ")("
#                 if s[i - 1] == ')' and dp[i - 1] >= 0:
#                     dp[i] = dp[i - 1]
#                 else:
#                     dp[i] = i
#         return global_max


# # 2. dp[i] to store the length of longest valid parentheses ending at i
# # O(n) and O(n)
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) <= 1:
#             return 0
#         maxlens = 0
#         dp = [0] * len(s)
#         for i in range(1, len(s)):
#             if s[i] == ')':
#                 # "()"
#                 if s[i - 1] == '(':
#                     if i >= 2:
#                         dp[i] = dp[i - 2] + 2
#                     else:
#                         dp[i] = 2
#                 # "))"
#                 elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
#                     if i - dp[i - 1] >= 2:
#                         dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
#                     else:
#                         dp[i] = dp[i - 1] + 2
#                 maxlens = max(maxlens, dp[i])
#         return maxlens


# # using stack: O(n) and O(n)
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         maxlens = 0
#         stack = [-1]
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     maxlens = max(maxlens, i - stack[-1])
#         return maxlens


# O(2n) and O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def _iter(from_left=True):
            maxlens = left = right = 0
            iter_range = range(len(s))
            if not from_left:
                iter_range = reversed(iter_range)
            for i in iter_range:
                if s[i] == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    maxlens = max(maxlens, left * 2)
                elif left < right and from_left or left > right and not from_left:
                    left = right = 0
            return maxlens

        return max(_iter(True), _iter(False))



# @lc code=end
