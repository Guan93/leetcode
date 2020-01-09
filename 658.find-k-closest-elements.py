#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from collections import deque


class Solution:
    # binary search: O(log(len(arr)) + k) and O(k)
    def findClosestElements(self, arr, k, x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= x:
                lo = mid + 1
            else:
                hi = mid

        smaller_ptr, larger_ptr = lo - 1, lo
        print(smaller_ptr, larger_ptr)
        res = deque()
        while len(res) < k:
            if (larger_ptr == len(arr)
                    or smaller_ptr >= 0 and x - arr[smaller_ptr] <= arr[larger_ptr] - x):
                res.appendleft(arr[smaller_ptr])
                smaller_ptr -= 1
            else:
                res.append(arr[larger_ptr])
                larger_ptr += 1
        return list(res)


# @lc code=end
