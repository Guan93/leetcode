class Solution:
    # # TLE
    # def knightDialer(self, N: int) -> int:
    #     from functools import lru_cache

    #     cords = set()
    #     for i in range(9):
    #         row, col = divmod(i, 3)
    #         cords.add((row, col))
    #     cords.add((3, 1))

    #     moves = [(2, 1), (1, 2), (-2, 1), (1, -2),
    #              (-1, 2), (2, -1), (-1, -2), (-2, -1)]

    #     @lru_cache(None)
    #     def _helper(cord, n):
    #         if n == 0:
    #             return 1
    #         count = 0
    #         for x_move, y_move in moves:
    #             new_cord = (cord[0] + x_move, cord[1] + y_move)
    #             if new_cord in cords:
    #                 count += _helper(new_cord, n - 1)
    #         return count

    #     count = 0
    #     for cord in cords:
    #         count += _helper(cord, N - 1)
    #     return count % (10 ** 9 + 7)

    def knightDialer(self, N):
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in xrange(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD