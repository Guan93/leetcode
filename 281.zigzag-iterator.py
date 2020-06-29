# Solution 1
from typing import List


class Node:
    def __init__(self, lst=[], idx=0, prev=None, next=None):
        self.idx = idx
        self.lst = lst
        self.prev_node = prev
        self.next_node = next

    def next(self):
        assert self.hasNext()
        val = self.lst[self.idx]
        self.idx += 1
        return val

    def hasNext(self):
        return self.idx < len(self.lst)


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        v = [_v for _v in [v1, v2] if len(_v) > 0]
        self.n = len(v)
        if self.n == 0:
            self.node = None
            return
        self.node = Node(v[0], 0)

        node = self.node
        for i in range(1, len(v)):
            nxt_node = Node(v[i])
            node.next_node = nxt_node
            nxt_node.prev_node = node
            node = nxt_node
        node.next_node = self.node
        self.node.prev_node = node

    def next(self) -> int:
        val = self.node.next()
        if not self.node.hasNext():
            if self.n > 2:
                self.node.prev_node.next_node = self.node.next_node
                self.node.next_node.prev_node = self.node.prev_node
                self.node = self.node.next_node
            elif self.n == 2:
                self.node = self.node.next_node
                self.node.next_node = None
                self.node.prev_node = None
            else:
                self.node = None
            self.n -= 1
        elif self.n > 1:
            self.node = self.node.next_node
        return val

    def hasNext(self) -> bool:
        return self.n > 0


# Solution 2
from collections import deque


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque([(v, 0) for v in [v1, v2] if v])

    def next(self) -> int:
        v, i = self.queue.popleft()
        val, i = v[i], i + 1
        if i < len(v):
            self.queue.append((v, i))
        return val

    def hasNext(self) -> bool:
        return len(self.queue) > 0
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())