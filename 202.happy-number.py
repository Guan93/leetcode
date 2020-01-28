#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    # # hash table: O(logn) and O(logn)
    # def isHappy(self, n: int) -> bool:
    #     def get_next(n):
    #         total_sum = 0
    #         while n > 0:
    #             n, rem = divmod(n, 10)
    #             total_sum += rem ** 2
    #         return total_sum

    #     seen = set()
    #     while n != 1 and n not in seen:
    #         seen.add(n)
    #         n = get_next(n)

    #     return n == 1

    # Floyd's Cycle-Finding Algorithm: O(logn) and O(1)
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, rem = divmod(n, 10)
                total_sum += rem ** 2
            return total_sum

        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
# @lc code=end
