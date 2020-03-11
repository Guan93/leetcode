#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    # brute force: O(mn) and O(1)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            nxt_gt = -1
            p = nums2.index(num)
            while p < len(nums2):
                if nums2[p] > num:
                    nxt_gt = nums2[p]
                    break
                p += 1
            res.append(nxt_gt)
        return res

    # monoqueue: O(m + n) and O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = dict()
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                res[stack.pop()] = num
            stack.append(num)

        return [res.get(num, -1) for num in nums1]

# @lc code=end

