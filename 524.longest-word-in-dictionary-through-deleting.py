#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#


# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for s0 in d:
            if self.canTransform(s, s0):
                if len(s0) > len(res) or len(s0) == len(res) and s0 < res:
                    res = s0

        return res

    def canTransform(self, long, short):
        i = j = 0
        while i < len(long) and j < len(short):
            if long[i] == short[j]:
                j += 1
            i += 1
        return j == len(short)


# @lc code=end
