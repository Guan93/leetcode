#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start

# # O(n) and O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        max_positive = 0
        for num in nums:
            max_positive = max(max_positive, num)
            seen.add(num)

        for i in range(1, max_positive + 1):
            if i not in seen:
                return i
        return max_positive + 1


# O(n) and O(1)
class Solution:
    def firstMissingPositive(self, nums):
        """
        Use index as a hash key and number sign as a presense detector.
        For example, if nums[1] is negative, it means that number '1' is
        present in the array; if nums[2] is positive, it means that number
        '2' is missing.
        """
        if 1 not in nums:
            return 1

        n = len(nums)
        # replace negative and numbers greater than n with 1 so that
        # only positive numbers are in the array.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


# O(n) and O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # put positive numbers to their correct positions
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1


# @lc code=end
