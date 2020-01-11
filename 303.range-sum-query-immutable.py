#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self._cumsum = [0]
        for num in nums:
            self._cumsum.append(self._cumsum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self._cumsum[j + 1] - self._cumsum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

