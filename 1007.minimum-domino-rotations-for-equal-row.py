#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#


# @lc code=start
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        counts = [0] * 6
        target = -1
        for i in range(N):
            counts[A[i] - 1] += 1
            if counts[A[i] - 1] >= N:
                target = A[i]
                break
            counts[B[i] - 1] += 1
            if counts[B[i] - 1] >= N:
                target = B[i]
                break
        if target == -1:
            return -1

        num_rotate_A = num_rotate_B = 0
        for i in range(N):
            if A[i] == target and B[i] == target:
                continue
            elif A[i] == target:
                num_rotate_B += 1
            elif B[i] == target:
                num_rotate_A += 1
            else:
                return -1
        return min(num_rotate_A, num_rotate_B)


# @lc code=end
