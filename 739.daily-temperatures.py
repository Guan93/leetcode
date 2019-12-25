#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:
    # brute force
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(T)):
    #         days = 0
    #         for j in range(i + 1, len(T)):
    #             if T[j] > T[i]:
    #                 days = j - i
    #                 break
    #         res.append(days)
    #     return res

    # next array, O(NW) (W is 102 in this case) and O(N + W)
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     res = [0] * len(T)
    #     last_seen = [len(T)] * 102  # temperature ranges from 30 - 100
    #     for i in range(len(T) - 1, -1, -1):
    #         closest_day = min([last_seen[t] for t in range(T[i] + 1, len(last_seen))])
    #         if closest_day < len(T):
    #             res[i] = closest_day - i
    #         last_seen[T[i]] = i
    #     return res

    # stack, O(N) and O(N)
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     res = [0] * len(T)
    #     stack = []  # store the indexes of temperatures
    #     for i in range(len(T)):
    #         while len(stack) > 0 and T[stack[-1]] < T[i]:
    #             index = stack.pop()
    #             res[index] = i - index
    #         stack.append(i)
    #     return res

    # stack, O(N) and O(W)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            # pop disordered indexes
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


# @lc code=end
