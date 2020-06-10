#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#


# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        for p in [p2, p3, p4]:
            if p1[0] == p[0] and p1[1] == p[1]:
                return False

        flag = self.is_equal_and_parallel(
            self.construct_vector(p1, p2), self.construct_vector(p3, p4))
        if flag == 0:
            p2, p3 = p3, p2
            flag = self.is_equal_and_parallel(
                self.construct_vector(p1, p2), self.construct_vector(p3, p4))
        if flag == 0:
            return False
        if flag == -1:
            p1, p2 = p2, p1

        v1 = self.construct_vector(p1, p2)
        v2 = self.construct_vector(p1, p3)
        return self.is_orthogonal(v1, v2) and self.has_same_length(v1, v2)

    def construct_vector(self, p1, p2):
        return [p2[0] - p1[0], p2[1] - p1[1]]

    def is_equal_and_parallel(self, v1, v2):
        """ Determine whether (p1, p2) and (p3, p4) is equal and parallel.
            Return 1 if in the same direction otherwise -1.
            Return 0 if not parallel or equal.
        """
        if v1[0] == v2[0] and v1[1] == v2[1]:
            return 1
        if v1[0] == -v2[0] and v1[1] == -v2[1]:
            return -1
        return 0

    def is_orthogonal(self, v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1] == 0

    def has_same_length(self, v1, v2):
        return v1[0]**2 + v1[1]**2 == v2[0]**2 + v2[1]**2


# @lc code=end
