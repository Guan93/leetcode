#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
import collections


# # O(N/W * N) and O(N)
# class Solution:
#     def isNStraightHand(self, hand: List[int], W: int) -> bool:
#         counts = collections.Counter(hand)
#         while counts:
#             m = min(counts)
#             for i in range(m, m + W):
#                 if i not in counts:
#                     return False
#                 elif counts[i] == 1:
#                     del counts[i]
#                 else:
#                     counts[i] -= 1
#         return True


# O(nlogn) and O(n)
class Solution:
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0

# @lc code=end
