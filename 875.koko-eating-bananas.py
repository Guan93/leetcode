#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def can_finish(K):
            spent_hours = 0
            for pile in piles:
                i, j = divmod(pile, K)
                spent_hours += i + (j > 0)
                if spent_hours > H:
                    return False
            return True

        lo, hi = 1, max(piles) + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not can_finish(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
# @lc code=end
