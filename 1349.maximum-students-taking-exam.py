# https://leetcode.com/problems/maximum-students-taking-exam/discuss/503686/A-simple-tutorial-on-this-bitmasking-problem
# dp with bitmask: O(m * 2^n) and O(m * 2^n)
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        valid_seats = list()
        for i in range(m):
            mask = 0
            for j in range(n):
                mask = mask * 2 + (seats[i][j] == '.')
            valid_seats.append(mask)

        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            curr_valid_seats = valid_seats[i - 1]
            for j in range(1 << n):
                if (j & curr_valid_seats) == j and not (j & (j >> 1)):
                    bit_count = bin(j).count('1')
                    for k in range(1 << n):
                        if dp[i - 1][k] >= 0 and not (j &
                                                      (k >> 1)) and not ((j >> 1) & k):
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + bit_count)

        return max(dp[-1])
