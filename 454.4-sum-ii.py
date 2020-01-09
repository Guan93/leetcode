#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from collections import Counter


class Solution:
    # O(n^2) and O(n)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = Counter()
        for num1 in A:
            for num2 in B:
                count[num1 + num2] += 1

        res = 0
        for num1 in C:
            for num2 in D:
                res += count[-(num1 + num2)]

        return res

# @lc code=end

