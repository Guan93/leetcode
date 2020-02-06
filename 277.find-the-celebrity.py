# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # # O(n^2) and O(1)
    # def findCelebrity(self, n: int) -> int:
    #     for i in range(n):
    #         count = 0
    #         for j in range(n):
    #             if i == j:
    #                 continue
    #             if not knows(j, i) or knows(i, j):
    #                 break
    #             count += 1
    #         if count == n - 1:
    #             return i
    #     return -1

    # O(n) and O(1)
    def findCelebrity(self, n):
        """
        Think of knows(a, b) as a <= b; not knows(a, b) as a > b;
        the problem is the same as finding the "largest person".
        """
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i

        if any([knows(x, i) and (x != i) or not knows(i, x) for i in range(n)]):
            return -1
        return x
