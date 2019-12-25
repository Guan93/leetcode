#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = self._iterate(S)
        stack2 = self._iterate(T)
        return stack1 == stack2

    def _iterate(self, s: str) -> List[str]:
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack

# @lc code=end
