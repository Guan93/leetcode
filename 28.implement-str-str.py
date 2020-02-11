#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    # O(L(N - L)) and O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # TODO: Rabin Karp algorithm (calculate hash rollingly in constant time)
        raise NotImplementedError

# @lc code=end

