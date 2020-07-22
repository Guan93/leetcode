# bisect: O(n^2) and O(n)
class Solution1:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        import bisect

        bulbs_on = []
        for i, bulb in enumerate(bulbs, start=1):
            pos = bisect.bisect_left(bulbs_on, bulb)
            # insert takes O(n) in python
            bulbs_on.insert(pos, bulb)
            if pos > 0 and bulbs_on[pos] - bulbs_on[pos - 1] == K + 1:
                return i
            if pos < len(bulbs_on) - 1 and bulbs_on[pos + 1] - bulbs_on[pos] == K + 1:
                return i

        return -1


# MinQueue: O(n) and O(n)
from collections import deque


class MinQueue(deque):
    def __init__(self):
        super().__init__()
        self.mins = deque()

    def popleft(self):
        x = super().popleft()
        if x == self.mins[0]:
            self.mins.popleft()
        return x

    def append(self, x):
        super().append(x)
        while self.mins and self.mins[-1] > x:
            self.mins.pop()
        self.mins.append(x)

    def min(self):
        return self.mins[0]


class Solution2:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        days = [0] * len(bulbs)
        for day, k in enumerate(bulbs, start=1):
            days[k - 1] = day

        mq = MinQueue()
        res = len(days)

        for i, day in enumerate(days):
            mq.append(day)
            if K <= i < len(days) - 1:
                mq.popleft()
                if K == 0 or days[i - K] < mq.min() > days[i + 1]:
                    res = min(res, max(days[i - K], days[i + 1]))

        return res if res < len(days) else -1


# sliding window: O(n) and O(n)
class Solution3:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        days = [0] * len(bulbs)
        for day, k in enumerate(bulbs, start=1):
            days[k - 1] = day

        lo, hi = 0, K + 1
        res = len(days)
        while hi < len(days):
            is_candidate = True
            for i in range(lo + 1, hi):
                if not (days[lo] < days[i] > days[hi]):
                    is_candidate = False
                    lo, hi = i, i + K + 1
                    break
            if is_candidate:
                res = min(res, max(days[lo], days[hi]))
                lo, hi = hi, hi + K + 1

        return res if res < len(days) else -1
