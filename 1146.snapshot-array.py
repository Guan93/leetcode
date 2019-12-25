#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [list() for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # note: (val1, ) < (val1, val2)
        i = bisect.bisect_right(self.snapshots[index], (snap_id + 1,)) - 1
        return self.snapshots[index][i][1] if i >= 0 else 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end
