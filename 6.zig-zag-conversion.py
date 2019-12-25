#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#


# @lc code=start
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s

    #     rows = [""] * numRows

    #     count = 0
    #     going_down = False
    #     for c in s:
    #         rows[count] += c
    #         if count == 0 or count == numRows - 1:
    #             going_down = not going_down
    #         count += 1 if going_down else -1
    #     res = ""
    #     for row in rows:
    #         res += row
    #     return res

    def convert(self, s: str, numRows: int) -> str:
        """
        elements in the first row: k * (numRows - 1) * 2
        elements in the last row: (2k - 1) * (numRows - 1)
        elements in the ith row other than the first and the last:
            first element: k * (numRows - 1) * 2 + i
            second element: (k + 1) * (numRows - 1) * 2 - i
        """
        if numRows == 1:
            return s
        res = ""
        # first row
        cycle_len = 2 * (numRows - 1)
        num_cycles = len(s) // cycle_len + 1
        for k in range(num_cycles):
            index = k * cycle_len
            res += (s[index] if index < len(s) else "")

        # ith row
        for i in range(1, numRows - 1):
            for k in range(num_cycles):
                first = s[k * cycle_len + i] if k * cycle_len + i < len(s) else ""
                second = s[(k + 1) * cycle_len -
                           i] if (k + 1) * cycle_len - i < len(s) else ""
                res = res + first + second

        # last row
        for k in range(num_cycles):
            index = k * cycle_len + numRows - 1
            res += (s[index] if index < len(s) else "")

        return res


# @lc code=end
