#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#


# @lc code=start
class Solution:
    # # dp: O(n) and O(n)
    # def numberOfArithmeticSlices(self, A: List[int]) -> int:
    #     dp = [0] * len(A)
    #     for i in range(2, len(A)):
    #         dp[i] = dp[i - 1] + 1 if A[i - 2] + A[i] == 2 * A[i - 1] else 0
    #     return sum(dp)

    # O(1) space dp
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        sum_ = count = 0
        for i in range(2, len(A)):
            if A[i - 2] + A[i] == 2 * A[i - 1]:
                count += 1
            else:
                sum_ += (count + 1) * count // 2
                count = 0
        sum_ += (count + 1) * count // 2
        return sum_


# @lc code=end
