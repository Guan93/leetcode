from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self._sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self._sum += val
        if len(self.queue) > self.size:
            self._sum -= self.queue.popleft()
        return self._sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)