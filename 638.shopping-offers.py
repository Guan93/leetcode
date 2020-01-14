#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#

# @lc code=start
from functools import lru_cache


class Solution:
    # # tle
    # def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    #     @lru_cache(None)
    #     def dfs(*needs):
    #         new_needs = []
    #         s = 0
    #         for need in needs:
    #             if need < 0:
    #                 return float("inf")
    #             s += need
    #             new_needs.append(need)
    #         if s == 0:
    #             return 0

    #         cost = float("inf")
    #         for i in range(len(price)):
    #             new_needs[i] -= 1
    #             if new_needs[i] >= 0:
    #                 cost = min(cost, price[i] + dfs(*new_needs))
    #             new_needs[i] += 1

    #         for offer in special:
    #             flag = True
    #             for i in range(len(needs)):
    #                 new_needs[i] -= offer[i]
    #                 if new_needs[i] < 0:
    #                     flag = False
    #             if flag:
    #                 cost = min(cost, offer[-1] + dfs(*new_needs))
    #             for i in range(len(needs)):
    #                 new_needs[i] += offer[i]
    #         return cost

    #     return dfs(*needs)

    # ac
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(None)
        def dfs(*needs):
            new_needs = []
            s = 0
            for need in needs:
                if need < 0:
                    return float("inf")
                s += need
                new_needs.append(need)
            if s == 0:
                return 0

            # calculate the minimum cost without special offers
            cost = 0
            for i in range(len(price)):
                cost += needs[i] * price[i]

            for offer in special:
                flag = True
                for i in range(len(needs)):
                    new_needs[i] -= offer[i]
                    if new_needs[i] < 0:
                        flag = False
                if flag:
                    cost = min(cost, offer[-1] + dfs(*new_needs))
                for i in range(len(needs)):
                    new_needs[i] += offer[i]
            return cost

        return dfs(*needs)
# @lc code=end

