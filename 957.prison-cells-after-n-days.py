#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#


# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def next_day(state):
            left = (state >> 1) & ((1 << 8) - 1)
            right = (state << 1) & ((1 << 8) - 1)
            res = (~(left ^ right)) & ((1 << 8) - 1)
            res &= ~1
            res &= ~(1 << 7)
            return res

        state = 0
        for i in range(8):
            state = state * 2 + cells[i]

        cycle = -1
        seen = {state: 0}
        for i in range(1, N + 1):
            state = next_day(state)
            if state in seen:
                cycle = i - seen[state]
                break
            seen[state] = i

        if cycle > 0:
            rest = N - i
            for j in range(rest % cycle):
                state = next_day(state)

        res = []
        for i in reversed(range(8)):
            res.append((state & (1 << i)) >> i)
        return res


# @lc code=end
