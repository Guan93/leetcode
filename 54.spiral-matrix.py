#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    # # O(mn) and O(mn)
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     def is_valid(x, y):
    #         return 0 <= x < m and 0 <= y < n and not seen[x][y]

    #     if not matrix:
    #         return []

    #     m, n = len(matrix), len(matrix[0])
    #     seen = [[False] * n for _ in range(m)]
    #     moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #     direction, (x, y) = 0, (0, 0)

    #     res = list()
    #     while True:
    #         seen[x][y] = True
    #         res.append(matrix[x][y])
    #         dx, dy = moves[direction]
    #         new_x, new_y = x + dx, y + dy
    #         if not is_valid(new_x, new_y):
    #             direction = (direction + 1) % 4
    #             dx, dy = moves[direction]
    #             new_x, new_y = x + dx, y + dy
    #         x, y = new_x, new_y
    #         if not is_valid(x, y):
    #             break

    #     return res

    # O(mn) and O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        bounds = [n - 1, m - 1, 0, 0]
        signs = [-1, -1, 1, 1]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction, (x, y) = 0, (0, 0)

        res = list()
        while True:
            res.append(matrix[x][y])
            dx, dy = moves[direction]
            new_x, new_y = x + dx, y + dy
            if not (bounds[3] <= new_x <= bounds[1] and bounds[2] <= new_y <= bounds[0]):
                bounds[(direction - 1) % 4] += signs[(direction - 1) % 4]
                direction = (direction + 1) % 4
                dx, dy = moves[direction]
                new_x, new_y = x + dx, y + dy
            x, y = new_x, new_y
            if not (bounds[3] <= x <= bounds[1] and bounds[2] <= y <= bounds[0]):
                break

        return res

# @lc code=end

