#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution:
    # dp: O(max(day)) and O(max(day))
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        last_day = max(days)
        mincosts = {0: 0}
        for day in range(1, last_day + 1):
            if day not in days_set:
                mincosts[day] = mincosts[day - 1]
            else:
                mincost = float("inf")
                for length, cost in zip([1, 7, 30], costs):
                    mincost = min(mincost, mincosts.get(day - length, 0) + cost)
                mincosts[day] = mincost
        return mincost
# @lc code=end

