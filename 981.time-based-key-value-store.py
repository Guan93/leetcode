#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

from bisect import bisect_right
# @lc code=start
from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        a = self._timemap[key]
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if timestamp < a[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return a[lo - 1][1] if lo > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
