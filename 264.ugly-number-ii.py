#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#


# @lc code=start
class Ugly:
    def __init__(self):
        self.nums = [1]
        primes = [2, 3, 5]
        ptrs = [0, 0, 0]
        for i in range(1690):
            next_ugly = min([self.nums[ptr] * prime for ptr, prime in zip(ptrs, primes)])
            for j in range(3):
                if self.nums[ptrs[j]] * primes[j] == next_ugly:
                    ptrs[j] += 1
            self.nums.append(next_ugly)


class Solution:
    pre_cal = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.pre_cal.nums[n - 1]

# @lc code=end

