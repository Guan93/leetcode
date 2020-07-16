#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = [c for c in s]
        vowels = {'a', 'o', 'i', 'e', 'u'}
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while s[lo] not in vowels:
                lo += 1
            while s[hi] not in vowels:
                hi -= 1
            if lo >= hi:
                break
            s_list[lo], s_list[hi] = s_list[hi], s_list[lo]
            lo, hi = lo + 1, hi - 1
        return ''.join(s_list)


# @lc code=end
