#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    # # brute force: O(n^2) and O(1)
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     for i in range(len(gas)):
    #         total_gas = num_stops = 0
    #         j = i
    #         can_travel = True
    #         while num_stops < len(gas):
    #             total_gas += gas[j] - cost[j]
    #             if total_gas < 0:
    #                 can_travel = False
    #                 break
    #             j = (j + 1) % len(gas)
    #             num_stops += 1
    #         if can_travel:
    #             return i
    #     return -1

    # one pass: O(n) and O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = deficit = idx = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            surplus += g - c
            if surplus < 0:
                deficit += surplus
                surplus = 0
                idx = i + 1
        return idx if surplus + deficit >= 0 else -1

# @lc code=end
