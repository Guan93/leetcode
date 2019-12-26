import collections

# # brute force: O(n!) and O(n)
# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:
#         accounts = collections.defaultdict(int)
#         for a, b, amount in transactions:
#             accounts[a] -= amount
#             accounts[b] += amount
#         debts = list(accounts.values())

#         def dfs(i):
#             while (i < len(debts) and debts[i] == 0):
#                 i += 1
#             if i == len(debts):
#                 return 0

#             ans = float("inf")
#             for j in range(i + 1, len(debts)):
#                 if debts[i] * debts[j] < 0:
#                     debts[j] += debts[i]
#                     ans = min(dfs(i + 1) + 1, ans)
#                     debts[j] -= debts[i]
#             return ans

#         return dfs(0)


# min_set O(n * 2^n) and O(2^n)
# https://leetcode.com/problems/optimal-account-balancing/discuss/219187/Short-O(N-*-2N)-DP-solution-with-detailed-explanation-and-complexity-analysis
class Solution:
    def minTransfers(self, transactions):
        persons = collections.defaultdict(int)
        for sender, receiver, amount in transactions:
            persons[sender] -= amount
            persons[receiver] += amount

        amounts = [amount for amount in persons.values() if amount != 0]

        N = len(amounts)
        dp = [0] * (2**N)  # dp[mask] = number of sets whose sum = 0
        sums = [0] * (2**N)  # sums[mask] = sum of numbers in mask

        for mask in range(2**N):
            set_bit = 1
            for b in range(N):
                if mask & set_bit == 0:
                    nxt = mask | set_bit
                    sums[nxt] = sums[mask] + amounts[b]
                    if sums[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[mask] + 1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[mask])
                set_bit <<= 1

        return N - dp[-1]
