#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#


# @lc code=start
# dp + binary search: O(nlogn) and O(n)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        endTime, startTime, profit = list(zip(*sorted(zip(endTime, startTime, profit))))
        # up to endTime[i], the max_profit attainable
        dp = [0] * len(endTime)
        for i in range(len(startTime)):
            dp[i] = profit[i]
            # dp is monotonic increasing, so we can use binary search
            lo, hi = 0, i
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if endTime[mid] <= startTime[i]:
                    lo = mid + 1
                else:
                    hi = mid
            idx = lo - 1
            if idx >= 0:
                dp[i] += dp[idx]
            if i > 0:
                dp[i] = max(dp[i - 1], dp[i])
        return dp[-1]


# @lc code=end
