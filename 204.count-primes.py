#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#


# @lc code=start
# # O(n^1.5)
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         res = 0

#         for i in range(2, n):
#             if self.isPrime(i):
#                 res += 1
#         return res

#     def isPrime(self, n):
#         if n < 2:
#             return False
#         i = 2
#         while i * i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True

# class Solution:
#     def countPrimes(self, n):
#         res = 0
#         is_prime = [True] * n
#         for i in range(2, n):
#             if is_prime[i]:
#                 res += 1
#                 next_num = i + i
#                 while next_num < n:
#                     is_prime[next_num] = False
#                     next_num += i
#         return res

# Sieve of Eratosthenes: O(nloglogn) and O(n)
class Solution:
    def countPrimes(self, n):
        res = 0
        is_prime = [True] * n
        i = 2
        while i * i < n:
            if is_prime[i]:
                res += 1
                next_num = i * i
                while next_num < n:
                    is_prime[next_num] = False
                    next_num += i
            i += 1
        for j in range(i, n):
            if is_prime[j]:
                res += 1
        return res


# @lc code=end
