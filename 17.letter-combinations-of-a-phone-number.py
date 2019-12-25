#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    MAP = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) > 0:
            self._letterCombinations(digits, 0, res, "")
        return res

    def _letterCombinations(self, digits: str, index: int, res: List[str], bt: str):
        if index == len(digits):
            res.append(bt)
            return

        for char in self.MAP[digits[index]]:
            self._letterCombinations(digits, index + 1, res, bt + char)


# @lc code=end
