class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, l, n = len(A), len(B), len(B[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            # here is the trick: we change the order of loop
            for k in range(l):
                if A[i][k] == 0:
                    continue
                for j in range(n):
                    if B[k][j] == 0:
                        continue
                    res[i][j] += A[i][k] * B[k][j]

        return res
