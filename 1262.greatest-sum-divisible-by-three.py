# dp
class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i]: the greatest sum so far where sum % 3 == i
        dp = [-float("inf")] * 3
        for num in nums:
            new_dp = [i for i in dp]
            rem = num % 3
            for i in range(3):
                j = (i + rem) % 3
                new_dp[j] = max(dp[j], dp[i] + num)
            dp = new_dp
            # fill the first num for rem
            if dp[rem] < 0:
                dp[rem] = num
        return dp[0] if dp[0] > 0 else 0


# concise
class Solution2:
    def maxSumDivThree(self, A):
        seen = [0, 0, 0]
        for a in A:
            for i in seen[:]:
                j = (i + a) % 3
                seen[j] = max(seen[j], i + a)
        return seen[0]