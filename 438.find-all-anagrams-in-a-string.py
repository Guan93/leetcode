#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
import collections


class Solution:
    # time limit exceeded
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     res = []
    #     p_sorted = tuple(sorted(p))
    #     for i in range(len(s) - len(p) + 1):
    #         if tuple(sorted(s[i:i + len(p)])) == p_sorted:
    #             res.append(i)
    #     return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        count_p, count_s = [0] * 26, [0] * 26
        for c in p:
            count_p[ord(c) - ord('a')] += 1
        for c in s[:len(p)]:
            count_s[ord(c) - ord('a')] += 1
        if count_s == count_p:
            res.append(0)
        for i in range(len(p), len(s)):
            to_delete = ord(s[i - len(p)]) - ord('a')
            to_add = ord(s[i]) - ord('a')
            count_s[to_delete] -= 1
            count_s[to_add] += 1
            if count_s == count_p:
                res.append(i - len(p) + 1)
        return res


# @lc code=end
