#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    num = num1 + num2
                elif token == '-':
                    num = num1 - num2
                elif token == '*':
                    num = num1 * num2
                elif token == '/':
                    num = int(num1 / num2)
                else:
                    raise ValueError("Invalid input!")
                stack.append(num)
        return stack[0]
# @lc code=end

