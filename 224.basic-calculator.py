#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque

        deq = deque()
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] in ['*', '/']:
                left = int(deq.pop())
                while s[i + 1] == ' ':
                    i += 1
                right = int(s[i + 1])
                if s[i] == '*':
                    deq.append(str(left * right))
                else:
                    deq.append(str(int(left / right)))
                i += 1
            else:
                deq.append(s[i])
            i += 1

        left = int(deq.popleft())
        while deq:
            op = deq.popleft()
            right = int(deq.popleft())
            if op == '+':
                left = left + right
            elif op == '-':
                left = left - right
        return left
# @lc code=end

