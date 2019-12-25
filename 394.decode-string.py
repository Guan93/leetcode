#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num, curr_str = 0, ""
        for c in s:
            if c == '[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num, curr_str = 0, ""
            elif c == ']':
                prev_str = stack.pop()
                num = stack.pop()
                curr_str = prev_str + curr_str * num
            elif c.isdigit():
                curr_num = curr_num * 10 + int(c)
            else:
                curr_str += c
        return curr_str


# @lc code=end
