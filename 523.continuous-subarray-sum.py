#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
# cumsum: O(n^2) and O(n)
class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumsum = [0]
        for num in nums:
            cumsum.append(cumsum[-1] + num)
        for end in range(2, len(nums) + 1):
            for start in range(end - 1):
                s = cumsum[end] - cumsum[start]
                if k == 0:
                    if s == 0:
                        return True
                elif s % k == 0:
                    return True
        return False


# hashmap: O(n) and O(n)
# a % c = k, b % c = k, (a - b) % c = 0
class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        rem_dict = {0: -1}
        for i, num in enumerate(nums):
            s += num
            if k != 0:
                s %= k
            if s in rem_dict:
                if i - rem_dict[s] > 1:
                    return True
            else:
                rem_dict[s] = i
        return False

# @lc code=end

