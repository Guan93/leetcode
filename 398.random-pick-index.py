#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import random
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self._counts = defaultdict(list)
        for i, num in enumerate(nums):
            self._counts[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self._counts[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
