#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        while n > 1:
            res = self._countAndSay(res)
            n -= 1
        return res

    def _countAndSay(self, num):
        res = []
        count = 1
        curr = num[0]
        for c in num[1:]:
            if c == curr:
                count += 1
            else:
                res.append(str(count))
                res.append(curr)
                curr = c
                count = 1
        res.append(str(count))
        res.append(curr)
        return ''.join(res)


# @lc code=end

