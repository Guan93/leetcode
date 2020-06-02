class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._timeline = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._timeline.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        bound = timestamp - 300
        lo, hi = 0, len(self._timeline)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self._timeline[mid] <= bound:
                lo = mid + 1
            else:
                hi = mid

        return len(self._timeline) - lo


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)