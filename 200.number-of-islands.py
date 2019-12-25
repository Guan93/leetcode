#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


# # dfs: O(m * n) and O(m * n) (worst case)
# class Solution:
#     def _dfs(self, grid, row, col):
#         m, n = len(grid), len(grid[0])
#         grid[row][col] = '0'
#         if row > 0 and grid[row - 1][col] == '1':
#             self._dfs(grid, row - 1, col)
#         if row < m - 1 and grid[row + 1][col] == '1':
#             self._dfs(grid, row + 1, col)
#         if col > 0 and grid[row][col - 1] == '1':
#             self._dfs(grid, row, col - 1)
#         if col < n - 1 and grid[row][col + 1] == '1':
#             self._dfs(grid, row, col + 1)

#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         if m == 0:
#             return 0
#         n = len(grid[0])

#         num_islands = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     self._dfs(grid, i, j)
#                     num_islands += 1
#         return num_islands


# bfs: O(m * n) and O(??)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        num_islands = 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
                    while queue:
                        row, col = queue.pop(0)
                        if row > 0 and grid[row - 1][col] == '1':
                            grid[row - 1][col] = '0'
                            queue.append((row - 1, col))
                        if row < m - 1 and grid[row + 1][col] == '1':
                            grid[row + 1][col] = '0'
                            queue.append((row + 1, col))
                        if col > 0 and grid[row][col - 1] == '1':
                            grid[row][col - 1] = '0'
                            queue.append((row, col - 1))
                        if col < n - 1 and grid[row][col + 1] == '1':
                            grid[row][col + 1] = '0'
                            queue.append((row, col + 1))
                    num_islands += 1
        return num_islands


# union find
# class UF:
#     def __init__(self, n: int) -> None:
#         self.count = n
#         self._parent = list(range(n))

#     def find(self, p: int) -> int:
#         while p != self._parent[p]:
#             p = self._parent[p]
#         return p

#     def is_connected(self, p: int, q: int) -> bool:
#         return self.find(p) == self.find(q)

#     def connect(self, p: int, q: int) -> None:
#         root_p = self.find(p)
#         root_q = self.find(q)
#         if root_p == root_q:
#             return
#         self._parent[root_p] = self._parent[root_q]
#         self.count -= 1

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         if m == 0:
#             return 0
#         n = len(grid[0])
#         uf = UF(m * n)

#         def _check_nearby(row, col):
#             if row > 0 and grid[row - 1][col] == '1':
#                 uf.connect((row - 1) * n + col, row * n + col)
#             if row < m - 1 and grid[row + 1][col] == '1':
#                 uf.connect((row + 1) * n + col, row * n + col)
#             if col > 0 and grid[row][col - 1] == '1':
#                 uf.connect(row * n + col - 1, row * n + col)
#             if col < n - 1 and grid[row][col + 1] == '1':
#                 uf.connect(row * n + col + 1, row * n + col)

#         count_zero = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '0':
#                     count_zero += 1
#                 else:
#                     _check_nearby(i, j)

#         return uf.count - count_zero

# @lc code=end
