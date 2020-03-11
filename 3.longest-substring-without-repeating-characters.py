#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # O(2n) and O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        lo = hi = max_len = 0
        while hi < len(s):
            if s[hi] not in curr_set:
                hi += 1
                curr_set.add(s[hi])
                max_len = max(max_len, hi - lo)
            else:
                curr_set.remove(s[lo])
                lo += 1
        return max_len

    # Optimized
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = dict()
        lo = max_len = 0
        for j, letter in enumerate(s):
            if letter in repeated and lo <= repeated[letter]:
                lo = repeated[letter] + 1
            else:
                max_len = max(max_len, j + 1 - lo)
            repeated[letter] = j
        return max_len
# @lc code=end

