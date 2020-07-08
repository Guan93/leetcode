# traverse one line at a time: O(mn) and O(mn)
class Solution1:
    def longestLine(self, M: List[List[int]]) -> int:
        def traverse(i, j, direction, seen):
            res = 1
            if direction == 'horizontal':
                dx, dy = 0, 1
            elif direction == 'vertical':
                dx, dy = 1, 0
            elif direction == 'diagonal':
                dx, dy = 1, 1
            elif direction == 'anti-diagonal':
                dx, dy = -1, 1

            seen[i][j] = True
            x, y = i + dx, j + dy

            while 0 <= x < m and 0 <= y < n:
                if M[x][y] == 0:
                    break
                res += 1
                seen[x][y] = True
                x, y = x + dx, y + dy

            return res

        if not M:
            return 0

        m, n = len(M), len(M[0])
        seen_h = [[False] * n for _ in range(m)]
        seen_v = [[False] * n for _ in range(m)]
        seen_d = [[False] * n for _ in range(m)]
        seen_a = [[False] * n for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                if not seen_h[i][j]:
                    res = max(res, traverse(i, j, 'horizontal', seen_h))
                if not seen_v[i][j]:
                    res = max(res, traverse(i, j, 'vertical', seen_v))
                if not seen_d[i][j]:
                    res = max(res, traverse(i, j, 'diagonal', seen_d))
                if not seen_a[i][j]:
                    res = max(res, traverse(i, j, 'anti-diagonal', seen_a))

        return res


class Solution2:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m, n = len(M), len(M[0])
        res = 0
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                dp[i][j][0] = 1 + (dp[i - 1][j][0] if i - 1 >= 0 else 0)
                dp[i][j][1] = 1 + (dp[i][j - 1][1] if j - 1 >= 0 else 0)
                dp[i][j][2] = 1 + (dp[i - 1][j - 1][2] if i - 1 >= 0 and j - 1 >= 0 else 0)
                dp[i][j][3] = 1 + (dp[i - 1][j + 1][3] if i - 1 >= 0 and j + 1 < n else 0)
                res = max(res, max(dp[i][j]))
        return res
