#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start

# from collections import Counter

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         counter1 = Counter()
#         counter2 = Counter()
#         numA = numB = 0
#         for i in range(len(secret)):
#             if secret[i] == guess[i]:
#                 numA += 1
#             counter1[secret[i]] += 1
#             counter2[guess[i]] += 1

#         for digit in (counter1 + counter2):
#             numB += abs(counter1[digit] - counter2[digit])
#         numB = int(len(secret) - numB / 2 - numA)
#         return f"{numA}A{numB}B"


# one pass
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        digits = [0] * 10
        for i in range(len(secret)):
            s, g = int(secret[i]), int(guess[i])
            if s == g:
                bull += 1
            else:
                if digits[s] < 0:
                    cow += 1
                if digits[g] > 0:
                    cow += 1
                digits[s] += 1
                digits[g] -= 1
        return f"{bull}A{cow}B"


# @lc code=end
