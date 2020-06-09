from collections import deque


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self._to_deque = 0
        self.capacity = capacity
        self.queue = deque()
        self._size = 0

    def enqueue(self, element: int) -> None:
        self.queue.append(element)
        if self._size < self.capacity:
            self._size += 1
        if self._to_deque > 0:
            self._to_deque -= 1
            self.dequeue()

    def dequeue(self) -> int:
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            self._to_deque += 1

    def size(self) -> int:
        return self._size
