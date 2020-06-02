class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(last, curr_len):
            if curr_len > n:
                return 0
            visited[last] = True
            count = 1 if curr_len >= m else 0
            for i in range(1, 10):
                if not visited[i] and (skips[last][i] == 0 or visited[skips[last][i]]):
                    count += dfs(i, curr_len + 1)
            visited[last] = False
            return count

        skips = [[0] * 10 for _ in range(10)]
        skips[1][3] = skips[3][1] = 2
        skips[1][7] = skips[7][1] = 4
        skips[7][9] = skips[9][7] = 8
        skips[3][9] = skips[9][3] = 6
        skips[2][8] = skips[8][2] = 5
        skips[4][6] = skips[6][4] = 5
        skips[1][9] = skips[9][1] = 5
        skips[3][7] = skips[7][3] = 5

        visited = [False] * 10
        return dfs(1, 1) * 4 + dfs(2, 1) * 4 + dfs(5, 1)