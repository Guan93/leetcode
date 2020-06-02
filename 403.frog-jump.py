#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#


# @lc code=start
# top-down dp: O(n^2) and O(n^2)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dp(pos, dist):
            if pos == 0:
                return dist == 1
            if (pos, dist) in memo:
                return memo[(pos, dist)]

            for dx in [-1, 0, 1]:
                new_dist = dist + dx
                new_pos = pos - new_dist
                if new_pos in stone_set and dp(new_pos, new_dist):
                    memo[(pos, dist)] = True
                    return True
            memo[(pos, dist)] = False
            return False

        stone_set = set(stones)
        memo = dict()
        for src in stones[:-1]:
            if dp(stones[-1], stones[-1] - src):
                return True
        return False
# @lc code=end
