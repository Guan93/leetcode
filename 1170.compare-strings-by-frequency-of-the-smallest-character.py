#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#

# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            counts = [0] * 26
            min_idx = ord(s[0]) - ord('a')
            for c in s:
                idx = ord(c) - ord('a')
                if idx <= min_idx:
                    min_idx = idx
                    counts[min_idx] += 1
            return counts[min_idx]

        def _binary_search(target, a):
            lo, hi = 0, len(a) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if target < a[mid]:
                    hi = mid - 1
                elif target >= a[mid]:
                    lo = mid + 1
            return len(a) - lo

        w_counts = sorted([f(word) for word in words])
        return [_binary_search(f(query), w_counts) for query in queries]
# @lc code=end
