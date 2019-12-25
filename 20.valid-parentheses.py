#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if p in parens:
                stack.append(parens[p])
            elif len(stack) == 0 or p != stack.pop():
                return False
        return len(stack) == 0

# @lc code=end
