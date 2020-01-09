#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
import bisect

class Solution:
    # binary search: O(mlogn) and O(1)
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            if idx == 0:
                res = max(res, heaters[0] - house)
            elif idx == len(heaters):
                res = max(res, house - heaters[-1])
            else:
                res = max(res, min(heaters[idx] - house, house - heaters[idx - 1]))
        return res


# @lc code=end

