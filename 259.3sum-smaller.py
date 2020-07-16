# binary search: O(n^2 logn) and O(1)
import bisect


class Solution1:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.twoSumSmaller(nums, i + 1, target - nums[i])

        return count

    def twoSumSmaller(self, nums, start, target):
        count = 0

        for i in range(start, len(nums) - 1):
            j = bisect.bisect_left(nums, target - nums[i], i + 1, len(nums))
            count += j - i - 1

        return count


# two pointers: O(n^2) and O(1)
class Solution2:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.twoSumSmaller(nums, i + 1, target - nums[i])

        return count

    def twoSumSmaller(self, nums, start, target):
        count = 0
        lo, hi = start, len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                count += hi - lo
                lo += 1
            else:
                hi -= 1

        return count
