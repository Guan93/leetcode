#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid_range(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return valid_range(s, i, j - 1) or valid_range(s, i + 1, j)
            i, j = i + 1, j - 1
        return True

# @lc code=end
