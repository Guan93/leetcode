#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n != 0:
            self._generateParenthesis(n, 0, 0, res, "")
        return res

    def _generateParenthesis(self, n: int, num_left: int, num_right: int, res: List[str],
                             bt: str) -> None:
        if num_left == n:
            res.append(bt + ')' * (n - num_right))
            return

        self._generateParenthesis(n, num_left + 1, num_right, res, bt + '(')
        if num_left > num_right:
            self._generateParenthesis(n, num_left, num_right + 1, res, bt + ')')


# @lc code=end
