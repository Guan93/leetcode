#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start

import bisect
import functools
import random


class Solution:

    def __init__(self, w: List[int]):
        # calculate the cumsum of weights
        self._w = []
        for ele in w:
            if not self._w:
                self._w.append(ele)
            else:
                self._w.append(self._w[-1] + ele)

    def pickIndex(self) -> int:
        i = random.randint(1, self._w[-1])
        return bisect.bisect_left(self._w, i)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
