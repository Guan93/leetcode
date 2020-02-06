#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            i, max_len = 0, min(len(s), len(prefix))
            while i < max_len:
                if s[i] != prefix[i]:
                    break
                i += 1
            prefix = prefix[:i]

        return prefix


# @lc code=end

