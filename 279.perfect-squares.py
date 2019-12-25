#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math


class Solution:
    # dp
    # def numSquares(self, n: int) -> int:
    #     square_nums = [i**2 for i in range(int(math.sqrt(n)) + 1)]
    #     dp = [float("inf")] * (n + 1)
    #     dp[0] = 0
    #     for i in range(1, n + 1):
    #         for square in square_nums:
    #             if i < square:
    #                 break
    #             dp[i] = min(dp[i], dp[i - square] + 1)
    #     return dp[-1]

    # greedy
    def numSquares(self, n: int) -> int:
        def is_divided_by(n: int, count: int) -> bool:
            if count == 1:
                return n in square_nums
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = [i**2 for i in range(int(math.sqrt(n)) + 1)]
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count
    
    # BFS
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(int(math.sqrt(n)) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square in square_nums:
                    if remainder == square:
                        return level
                    elif remainder < square:
                        break
                    else:
                        next_queue.add(remainder - square)
            queue = next_queue
        return level



# @lc code=end
