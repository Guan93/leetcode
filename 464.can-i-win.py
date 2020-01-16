#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        def dfs(nums, target, cache):
            if nums in cache:
                return cache[nums]

            if nums[-1] >= target:
                return True

            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i + 1:]
                if not dfs(new_nums, target - nums[i], cache):
                    cache[nums] = True
                    return True
            cache[nums] = False
            return False
        cache = dict()
        return dfs(tuple(i for i in range(1, maxChoosableInteger + 1)), desiredTotal, cache)


# @lc code=end

