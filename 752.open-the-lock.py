#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
import collections


# bfs: transform the problem to a shortest path problem
# Complexity: O(N^2 * A^N + D)
# where, N is Number of dials (4 in our case)
# A is number of alphabets (10 in our case -> 0 to 9)
# D is the size of deadends.

# There are 10 x 10 x 10 x 10 possible combinations => 10^4 => A^N
# For each combination, we are looping 4 times (which is N) and in each iteration,
# there are substring operations ( which is O(N) * constant) => O(4N*constant) => O(4N) => O(NN) => O(N^2)
# Total complexity => A^N * N^2, plus D to create the hashset => N^2 * A^N + D
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_adj(wheels):
            res = []
            for i in range(len(wheels)):
                res.append(wheels[:i] + str((int(wheels[i]) + 1) % 10) + wheels[i + 1:])
                res.append(wheels[:i] + str((int(wheels[i]) - 1) % 10) + wheels[i + 1:])

            return res

        deadends = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in deadends: continue
            for nei in get_adj(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


# @lc code=end
