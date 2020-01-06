#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def _myPow(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            is_odd = n % 2 == 1
            half_n = n // 2
            half_res = _myPow(half_n)
            return half_res * half_res * x if is_odd else half_res * half_res

        res = _myPow(abs(n))
        return res if n >= 0 else 1 / res

# @lc code=end

