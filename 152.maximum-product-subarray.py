#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#


# @lc code=start
class Solution:
    # dp: O(n) and O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = nums[0]
        global_max_prod = nums[0]
        for i in range(1, len(nums)):
            prod1 = max_prod * nums[i]
            prod2 = min_prod * nums[i]
            max_prod = max(max(prod1, prod2), nums[i])
            min_prod = min(min(prod1, prod2), nums[i])
            global_max_prod = max(max_prod, global_max_prod)
        return global_max_prod

    # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/In-Python-it-can-be-more-concise-PythonC%2B%2BJava
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


# @lc code=end
