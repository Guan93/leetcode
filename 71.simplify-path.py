#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for symbol in path.split('/'):
            if len(symbol) == 0 or symbol == '.':
                continue
            elif symbol == '..':
                if res:
                    res.pop()
            else:
                res.append(symbol)

        return '/' + '/'.join(res)


# @lc code=end
