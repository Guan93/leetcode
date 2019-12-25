#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        curr_min = self.getMin()
        if curr_min is None or x < curr_min:
            curr_min = x
        # we store a tuple in the stack to keep track of the min values
        self._stack.append((x, curr_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        if len(self._stack) > 0:
            return self._stack[-1][0]

    def getMin(self) -> int:
        if len(self._stack) > 0:
            return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
