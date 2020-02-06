#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def is_parlindrome(self, s):
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        if s == 0:
            return res

        for end in range(len(s)):
            if s[end] != s[0]:
                continue
            target_word = s[0:end + 1]
            if self.is_parlindrome(target_word):
                curr_partition = [target_word]
                if end < len(s) - 1:
                    for p in self.partition(s[end + 1:]):
                        res.append(curr_partition + p)
                else:
                    res.append(curr_partition)
        return res
# @lc code=end
