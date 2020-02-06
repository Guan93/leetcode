#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    # # 3 iteration and two times space
    # def calculate(self, s: str) -> int:
    #     from collections import deque

    #     clean_list = []
    #     i = 0
    #     while i < len(s):
    #         if s[i] == ' ':
    #             i += 1
    #             continue
    #         if s[i] in ['*', '/', '+', '-']:
    #             clean_list.append(s[i])
    #             i += 1
    #         else:
    #             num = 0
    #             while i < len(s) and s[i].isdigit():
    #                 num = num * 10 + int(s[i])
    #                 i += 1
    #             clean_list.append(num)

    #     i = 0
    #     deq = deque()
    #     while i < len(clean_list):
    #         if clean_list[i] in ['*', '/']:
    #             left = deq.pop()
    #             op = clean_list[i]
    #             right = clean_list[i + 1]
    #             i += 1
    #             if op == '*':
    #                 deq.append(left * right)
    #             elif op == '/':
    #                 deq.append(int(left / right))
    #         else:
    #             deq.append(clean_list[i])
    #         i += 1

    #     left = deq.popleft()
    #     while deq:
    #         op = deq.popleft()
    #         right = deq.popleft()
    #         if op == '+':
    #             left = left + right
    #         elif op == '-':
    #             left = left - right
    #     return left

    # # O(N) and O(N)
    # def calculate(self, s: str) -> int:
    #     num, stack, pre_op = 0, [], '+'
    #     for c in s + '+':
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         elif not c.isspace():
    #             if pre_op == '+':
    #                 stack.append(num)
    #             elif pre_op == '-':
    #                 stack.append(-num)
    #             elif pre_op == '*':
    #                 stack.append(stack.pop() * num)
    #             elif pre_op == '/':
    #                 stack.append(int(stack.pop() / num))
    #             pre_op, num = c, 0
    #     return sum(stack)

    # O(N) and O(1)
    def calculate(self, s: str) -> int:
        res, num, prev_num, pre_op = 0, 0, 0, '+'
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif not c.isspace():
                if pre_op == '-':
                    num = -num
                elif pre_op == '*':
                    res -= prev_num
                    num = prev_num * num
                elif pre_op == '/':
                    res -= prev_num
                    num = int(prev_num / num)
                res, pre_op, prev_num, num = res + num, c, num, 0
        return res
# @lc code=end
