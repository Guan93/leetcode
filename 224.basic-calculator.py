#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc code=start
# stack: O(n) and O(n)
class Solution1:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'

        stack = []
        for c in s:
            if c == ')':
                inner_res = 0
                while True:
                    num = int(stack.pop())
                    symbol = stack.pop()
                    if symbol == '-':
                        inner_res -= num
                    else:
                        inner_res += num
                        if symbol == '(':
                            break
                stack.append(str(inner_res))
            elif c == ' ':
                continue
            elif c.isnumeric() and stack and stack[-1].isnumeric():
                stack[-1] += c
            else:
                stack.append(c)
        return stack[0]


# stack with reverse string O(n) and O(n)
class Solution2:
    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)


# @lc code=end
