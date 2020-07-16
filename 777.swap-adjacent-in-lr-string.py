#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#


# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def helper(s):
            res = []
            for i, c in enumerate(s):
                if c == 'X':
                    continue
                res.append((c, i))
            return res

        if len(start) != len(end):
            return False

        ind_s = helper(start)
        ind_e = helper(end)
        if len(ind_s) != len(ind_e):
            return False

        for pair1, pair2 in zip(ind_s, ind_e):
            if pair1[0] != pair2[0]:
                return False
            c = pair1[0]
            if c == 'L' and pair1[1] < pair2[1] or c == 'R' and pair1[1] > pair2[1]:
                return False

        return True


# @lc code=end
