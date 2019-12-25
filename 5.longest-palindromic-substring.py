#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    # from center
    # def longestPalindrome(self, s: str) -> str:
    #     res = ""
    #     for i in range(len(s)):
    #         # odd case such as "aba"
    #         tmp = self._longest_palindrome(s, i, i)
    #         res = tmp if len(tmp) > len(res) else res
    #         # even case such as "abba"
    #         tmp = self._longest_palindrome(s, i, i + 1)
    #         res = tmp if len(tmp) > len(res) else res
    #     return res

    # def _longest_palindrome(self, s: str, left: int, right: int) -> str:
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left, right = left - 1, right + 1
    #     return s[left + 1:right]

    # dp
    def longestPalindrome(self, s: str) -> str:
        # 1. create a 2D array: dp[i][j] is true if s[i:j+1] is palindrome
        dp = [[False] * len(s) for _ in range(len(s))]
        # 2. initiate results
        global_start = global_end = 0
        # 3. dp
        for i in range(len(s)):
            start = end = i
            while start >= 0:
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and s[start] == s[end]
                if end - start > global_end - global_start and dp[start][end]:
                    global_start, global_end = start, end
                start -= 1
        return s[global_start:global_end + 1]


# @lc code=end
