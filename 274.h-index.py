#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
# O(nlogn) and O(1)
class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        lo, hi = 0, len(citations)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] >= mid + 1:
                lo = mid + 1
            else:
                hi = mid
        return lo


# O(n) and O(n)
class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)

        for c in citations:
            counts[min(c, n)] += 1

        k = n
        s = counts[n]
        while k > s:
            k -= 1
            s += counts[k]

        return k


# @lc code=end
