#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
# O(n^2) and O(n)
# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         res = [None] * len(people)
#         people.sort(key=lambda x: (x[0], -x[1]))
#         for p in people:
#             num_nones = 0
#             for i in range(len(res)):
#                 if num_nones == p[1] and res[i] is None:
#                     break
#                 if res[i] is None:
#                     num_nones += 1
#             res[i] = p
#         return res


# O(n^2) and O(n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


# @lc code=end
