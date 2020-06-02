#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#


# @lc code=start
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            if num != i + 1:
                if nums[num - 1] == num:
                    nums[i] = 0
                    res.append(num)
                    i += 1
                else:
                    if nums[num - 1] > 0:
                        nums[i], nums[num - 1] = nums[num - 1], nums[i]
                    else:
                        nums[num - 1] = nums[i]
                        nums[i] = 0
                        i += 1
            else:
                i += 1
        return res


class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[num - 1] < 0:
                res.append(num)
            nums[num - 1] *= -1
        return res
# @lc code=end
