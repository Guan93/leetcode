#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start


# binary search
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def _possible_to_ship(cap):
            days = cur_sum = 0
            for weight in weights:
                if weight > cap:
                    return False
                if cur_sum + weight <= cap:
                    cur_sum += weight
                else:
                    cur_sum = weight
                    days += 1
            if cur_sum <= cap:
                days += 1
            return days <= D

        lo, hi = int(sum(weights) / D) - 1, sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if _possible_to_ship(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi

    # def shipWithinDays(self, a: List[int], d: int) -> int:
    #         lo, hi = max(a), sum(a)   
    #         while lo < hi:
    #             mid = (lo + hi) // 2
    #             tot, res = 0, 1
    #             for wt in a:
    #                 if tot + wt > mid:
    #                     res += 1
    #                     tot = wt
    #                 else:
    #                     tot += wt
    #             if res <= d:
    #                 hi = mid
    #             else:
    #                 lo = mid+1
    #         return lo


# @lc code=end
