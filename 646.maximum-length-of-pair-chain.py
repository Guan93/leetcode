#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
#     # dp: O(n^2) and O(n)
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         n = len(pairs)
#         dp = [1] * n
#         for j in range(n):
#             for i in reversed(range(j)):
#                 if pairs[i][1] < pairs[j][0]:
#                     dp[j] = dp[i] + 1
#                     break
#         return dp[-1]

    # greedy: O(nlogn) and O(n)(to store the sorted array)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = float("-inf"), 0
        for first, second in sorted(pairs, key=lambda x: x[1]):
            if cur < first:
                cur = second
                ans += 1
        return ans

# @lc code=end

