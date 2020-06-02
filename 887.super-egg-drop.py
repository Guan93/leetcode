#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#


# @lc code=start
class Solution:
    # O(kn^2) and O(kn)
    def superEggDrop(self, K: int, N: int) -> int:
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float("inf")
            for i in range(1, N + 1):
                res = min(res, max(dp(K - 1, i - 1), dp(K, N - i)) + 1)
            memo[(K, N)] = res
            return res

        memo = dict()
        return dp(K, N)

    # O(knlogn) and O(kn)
    def superEggDrop(self, K: int, N: int) -> int:
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float("inf")
            lo, hi = 1, N + 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken <= not_broken:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
                else:
                    hi = mid
                    res = min(res, broken + 1)
            if lo <= N:
                res = min(res, dp(K - 1, lo - 1) + 1)
            memo[(K, N)] = res
            return res

        memo = dict()
        return dp(K, N)


# @lc code=end
