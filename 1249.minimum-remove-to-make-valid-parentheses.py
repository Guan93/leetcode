class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res, stack = [], []
        for i, c in enumerate(s):
            res.append(c)
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    res[-1] = ''

        for i in stack:
            res[i] = ''

        return ''.join(res)
