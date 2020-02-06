#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        for letter in counts:
            if counts[letter] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(letter))
        return len(s)
# @lc code=end

