#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    # use divide
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count_of_zeros = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                count_of_zeros += 1

        if count_of_zeros == 0:
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
        elif count_of_zeros == 1:
            for i in range(len(nums)):
                nums[i] = prod if nums[i] == 0 else 0
        else:
            nums = [0] * len(nums)
        return nums

    # without divide, space complexity O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R = [1] * n, [1] * n
        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]

        ans = []
        for i in range(n):
            ans.append(L[i] * R[i])
        return ans

    # without divide, space complexity O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = 1
        n = len(nums)
        ans = [1] * n  # use ans to replace R and construct L on the fly
        for i in range(n - 2, -1, -1):
            ans[i] = ans[i + 1] * nums[i + 1]
        for i in range(1, n):
            L *= nums[i - 1]
            ans[i] *= L
        return ans


# @lc code=end
