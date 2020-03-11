#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    # dp: O(n^2) and O(n^2)
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s)):
            start = end = i
            while start >= 0:
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and s[start] == s[end]
                if dp[start][end]:
                    count += 1
                start -= 1
        return count

    # start from the center: O(n^2) and O(1)
    def countSubstrings(self, s: str) -> int:
        def _helper(start, end, s):
            count = 0
            while start >= 0 and end < len(s):
                if s[start] != s[end]:
                    break
                count += 1
                start, end = start - 1, end + 1
            return count

        count = 0
        for center in range(len(s)):
            count = count + _helper(center, center, s) + _helper(center, center + 1, s)

        return count
# @lc code=end
