#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
# one character at a time
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


# another implementation: one number / word at a time
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            curr = ""
            if s[i].isdigit():
                while s[i].isdigit():
                    curr += s[i]
                    i += 1
            elif s[i].isalpha():
                while i < len(s) and s[i].isalpha():
                    curr += s[i]
                    i += 1
            elif s[i] == ']':
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                num = int(stack.pop())
                curr *= num
                i += 1
            else:
                curr = s[i]
                i += 1
            stack.append(curr)
        return "".join(stack)

# @lc code=end
