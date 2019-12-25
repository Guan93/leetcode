#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#


# # @lc code=start
class Solution:
    _min_removed = float('inf')

    def removeInvalidParentheses(self, s: str) -> List[str]:
        def _helper(i, acc, diff, num_removed):
            if num_removed > self._min_removed:
                return
            if i == len(s):
                if diff == 0 and len(acc) > 0:
                    res.append(acc)
                    self._min_removed = num_removed
                return
            if s[i] == '(':
                _helper(i + 1, acc + s[i], diff + 1, num_removed)
            elif s[i] == ')':
                if diff > 0:
                    _helper(i + 1, acc + s[i], diff - 1, num_removed)
            else:
                _helper(i + 1, acc + s[i], diff, num_removed)
            _helper(i + 1, acc, diff, num_removed + 1)

        res = []
        _helper(0, "", 0, 0)
        return list(set(res)) if res else [""]


# @lc code=end
