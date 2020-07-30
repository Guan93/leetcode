#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        def dfs(r, c):
            res[r][c] = newColor
            visited[r][c] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = r + dx, c + dy
                if (0 <= x < m and 0 <= y < n and not visited[x][y]
                        and image[x][y] == start_color):
                    dfs(x, y)

        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        visited = [[False] * n for _ in range(m)]
        res = [[image[i][j] for j in range(n)] for i in range(m)]
        dfs(sr, sc)

        return res


# @lc code=end
