#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#


# @lc code=start
# brute force: O(n^2) and O(n)
class Solution1:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumsum = [0]
        for num in A:
            cumsum.append(cumsum[-1] + num)

        res = 0
        for s1 in range(len(A) - L + 1):
            e1 = s1 + L
            for s2 in range(len(A) - M + 1):
                e2 = s2 + M
                if s1 < e2 and s2 < e1:
                    continue
                res = max(cumsum[e1] - cumsum[s1] + cumsum[e2] - cumsum[s2], res)

        return res


# two-pass O(n) and O(n)
class Solution2:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumsum = [0]
        for num in A:
            cumsum.append(cumsum[-1] + num)

        res = 0
        Lmax = Mmax = 0
        for i in range(L + M, len(A) + 1):
            Lmax = max(Lmax, cumsum[i - M] - cumsum[i - M - L])
            Mmax = max(Mmax, cumsum[i - L] - cumsum[i - M - L])
            res = max(res, Lmax + cumsum[i] - cumsum[i - M],
                      Mmax + cumsum[i] - cumsum[i - L])

        return res


# @lc code=end
