#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start

# O(n^2) and O(n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        res = [None] * len(people)

        for h, k in people:
            count = k
            for i in range(len(res)):
                if res[i] is None:
                    if count == 0:
                        res[i] = [h, k]
                        break
                    else:
                        count -= 1

        return res


# O(n^2) and O(n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


# @lc code=end
