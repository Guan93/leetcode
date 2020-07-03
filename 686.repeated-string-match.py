#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#


# @lc code=start
# O((M + N) * N) and O(M + N), where M = len(A) and N = len(B)
class Solution:
    def repeatedStringMatch(self, A, B):
        # q = ceil(len(B) / len(A))
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1


# @lc code=end
