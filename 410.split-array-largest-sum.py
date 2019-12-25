#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
# # brute force: O(C(n-1, m-1))
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         self.ans = float("inf")
#         n = len(nums)

#         def dfs(curr_idx, curr_m, curr_max, curr_sum):
#             if curr_idx == n and curr_m == m:
#                 self.ans = min(self.ans, curr_max)
#             if curr_idx == n:
#                 return
#             if curr_m == m:
#                 self.ans = min(max(curr_sum + sum(nums[curr_idx:]), curr_max), self.ans)
#             else:
#                 if curr_idx > 0:
#                     dfs(curr_idx + 1, curr_m, max(curr_max, curr_sum + nums[curr_idx]), curr_sum + nums[curr_idx])
#                 dfs(curr_idx + 1, curr_m + 1, max(curr_max, nums[curr_idx]), nums[curr_idx])
#             return

#         dfs(0, 0, -float("inf"), 0)
#         return self.ans


# # dp:O(mn^2) O(mn) TLE
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
#         dp[0][0] = 0
#         cumsum = [0] * (n + 1)

#         for i in range(n):
#             cumsum[i + 1] = cumsum[i] + nums[i]

#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 for k in range(0, i):
#                     dp[i][j] = min(dp[i][j], max(dp[k][j - 1], cumsum[i] - cumsum[k]))

#         return dp[-1][-1]


# binary search with greedy: O(nlog(sum(nums))) and O(1)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        ans = r
        while l <= r:
            mid = (r - l) // 2 + l
            cnt, curr_sum = 1, 0
            for num in nums:
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    cnt += 1
                    curr_sum = num
                if cnt > m:
                    l = mid + 1
                    break
            if cnt <= m:
                r = mid - 1
                ans = min(ans, mid)
        return ans

# @lc code=end
