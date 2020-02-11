class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = v
        self.nrow = len(v)
        self.curr_row = 0
        self.curr_col = -1
        self._findNext()

    def next(self) -> int:
        next_val = self.v[self.curr_row][self.curr_col]
        self._findNext()
        return next_val

    def hasNext(self) -> bool:
        return self.curr_row < self.nrow and self.curr_col < len(self.v[self.curr_row])

    def _findNext(self):
        while self.curr_row < self.nrow:
            self.curr_col += 1
            if self.curr_col < len(self.v[self.curr_row]):
                break
            else:
                self.curr_row += 1
                self.curr_col = 0

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()