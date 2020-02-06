#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    # divide and conquer: O(nlogn) (can be derived by master theorem) and O(n)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        left = self.getSkyline(buildings[:n // 2])
        right = self.getSkyline(buildings[n // 2:])
        return self.mergeSkyline(left, right)

    def mergeSkyline(self, left, right):
        def update(x, y):
            if not output or x != output[-1][0]:
                output.append([x, y])
            else:
                output[-1][1] = y

        def append(p, skyline, curr_y):
            while p < len(skyline):
                x, y = skyline[p]
                if curr_y != y:
                    update(x, y)
                    curr_y = y
                p += 1

        output = []
        n_left, n_right = len(left), len(right)
        p_left = p_right = 0
        left_y = right_y = curr_y = 0


        while p_left < n_left and p_right < n_right:
            point_left, point_right = left[p_left], right[p_right]
            if point_left[0] < point_right[0]:
                x, left_y = point_left
                p_left += 1
            else:
                x, right_y = point_right
                p_right += 1

            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update(x, max_y)
                curr_y = max_y

        append(p_left, left, curr_y)
        append(p_right, right, curr_y)

        return output
# @lc code=end

