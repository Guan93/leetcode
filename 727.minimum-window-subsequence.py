# dp: O(mn) and O(mn)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(T), len(S)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        start, length = 0, float("inf")
        for j in range(1, n + 1):
            if dp[-1][j] != 0 and j - dp[-1][j] + 1 < length:
                start, length = dp[-1][j] - 1, j - dp[-1][j] + 1
        
        return S[start: start + length] if length < float("inf") else ""
