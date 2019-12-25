#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

# # heap: O(nlogn) and O(1)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k - 1]

# # O(nlogk) and O(k)
# import heapq

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]

# quick select: O(n) in average O(n^2) in the worst case; O(1)
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def _partition(left: int, right: int, pivot_index: int) -> int:
            pivot = nums[pivot_index]

            # 1. move pivot to the end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1

            # 3. move pivot to its final position
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def _select(left: int, right: int, k: int) -> int:
            """
            Return the k-th smallest elements of list within left...right.
            """
            if left == right:
                return nums[left]
            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = _partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k < pivot_index:
                return _select(left, pivot_index - 1, k)
            elif k > pivot_index:
                return _select(pivot_index + 1, right, k)
            else:
                return nums[k]

        return _select(0, len(nums) - 1, len(nums) - k)
# @lc code=end
