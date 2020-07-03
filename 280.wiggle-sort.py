class Solution1:
    # O(nlogn) and O(1)
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) <= 2:
            return nums

        i = 1
        while i + 1 < len(nums):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        return nums


# one-pass: O(n) and O(1)
class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        up = True
        for i in range(len(nums) - 1):
            if up and nums[i] > nums[i + 1] or not up and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            up = not up

        return nums
