#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#


# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:
        max_char, max_count = '', 0
        count = dict()
        for c in S:
            count[c] = count.get(c, 0) + 1
            if count[c] > max_count:
                max_char, max_count = c, count[c]
        if max_count > len(S) / 2:
            return ""

        res = [max_char for _ in range(max_count)]
        p = 0
        for c in count:
            if c == max_char:
                continue
            for _ in range(count[c]):
                res[p] = res[p] + c
                p = (p + 1) % max_count
        return ''.join(res)


# @lc code=end
