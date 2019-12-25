#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#


# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n <= 1:
            return 0
        # swap[i] represents the min swaps to make A[:i] and B[:i] increasing
        # if we swap A[i] and B[i]; nonswap if we do not swap A[i] and B[i] 
        swap = [1] + [n] * (n - 1)
        nonswap = [0] + [n] * (n - 1)
        for i in range(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                nonswap[i] = nonswap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                nonswap[i] = min(nonswap[i], swap[i - 1])
                swap[i] = min(nonswap[i - 1] + 1, swap[i])
        return min(swap[-1], nonswap[-1])
# @lc code=end
