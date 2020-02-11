#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#


# @lc code=start
class Solution:
    # # O(n) and O(n)
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     k = k % len(nums)
    #     if k > 0:
    #         nums[:k], nums[k:] = nums[-k:], nums[:-k]

    # # reverse three times: O(n) and O(1)
    # def rotate(self, nums, k):
    #     def reverse(nums, lo, hi):
    #         while lo <= hi:
    #             nums[lo], nums[hi] = nums[hi], nums[lo]
    #             lo, hi = lo + 1, hi - 1

    #     k = k % len(nums)
    #     if k > 0:
    #         reverse(nums, 0, len(nums) - 1)
    #         reverse(nums, 0, k - 1)
    #         reverse(nums, k, len(nums) - 1)

    # cyclic replacements: O(n) and O(1)
    def rotate(self, nums, k):
        n, k = len(nums), k % len(nums)
        count = 0
        start = 0
        while count < n:
            curr, tmp = (start + k) % n, nums[start]
            tmp, nums[curr] = nums[curr], tmp
            count += 1
            while curr != start:
                nxt = (curr + k) % n
                tmp, nums[nxt] = nums[nxt], tmp
                curr = nxt
                count += 1
            start += 1



# @lc code=end
