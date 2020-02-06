#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        l = list()
        for i, c in enumerate(s):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                l.append(i)

        for i in l:
            if d[s[i]] == 1:
                return i
        return -1

# @lc code=end

