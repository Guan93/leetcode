#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#


# @lc code=start
# top-down dp: O(len(s1) * len(s2)) and O(len(s1) * len(s2))
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            k = i + j
            if i == 0 and j == 0:
                return True
            elif i == 0:
                memo[(i, j)] = dp(i, j - 1) and s2[j - 1] == s3[k - 1]
            elif j == 0:
                memo[(i, j)] = dp(i - 1, j) and s1[i - 1] == s3[k - 1]
            else:
                memo[(i, j)] = (dp(i - 1, j) and s1[i - 1] == s3[k - 1]
                                or dp(i, j - 1) and s2[j - 1] == s3[k - 1])
            return memo[(i, j)]

        if len(s1) + len(s2) != len(s3):
            return False
        memo = dict()
        return dp(len(s1), len(s2))


# @lc code=end
