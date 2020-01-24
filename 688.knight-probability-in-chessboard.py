#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    # # O(N^2 * K) and O(N^2 * K)
    # def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def _helper(x, y, k):
    #         if k == 0:
    #             return 1

    #         prob = 0
    #         for x_move, y_move in moves:
    #             new_x, new_y = x + x_move, y + y_move
    #             if 0 <= new_x < N and 0 <= new_y < N:
    #                 prob += _helper(new_x, new_y, k - 1) / 8
    #         return prob

    #     moves = [(2, 1), (1, 2), (-2, 1), (1, -2),
    #              (-1, 2), (2, -1), (-1, -2), (-2, -1)]
    #     return _helper(r, c, K)

    # dp: O(N^2 * K) and O(N^2)
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (1, -2),
                 (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1

        for _ in range(K):
            _dp = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in moves:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < N and 0 <= new_c < N:
                            _dp[new_r][new_c] += val / 8
            dp = _dp
        return sum(map(sum, dp))

# @lc code=end

