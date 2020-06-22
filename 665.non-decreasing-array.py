#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#


# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        has_changed = False
        for i in range(len(nums) - 1):
            curr, nxt = nums[i], nums[i + 1]
            if curr > nxt:
                if has_changed:
                    return False
                # we have two options: change curr value to nxt or nxt to curr
                prev = nums[i - 1] if i > 0 else -float("inf")
                if nxt >= prev:
                    nums[i] = nxt
                else:
                    nums[i + 1] = curr
                has_changed = True
        return True


# @lc code=end
