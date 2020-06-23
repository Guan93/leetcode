#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#


# @lc code=start
class Solution:
    def totalFruit(self, tree) -> int:
        if not tree:
            return 0
        if len(tree) == 1:
            return 1

        first = tree[0]
        last_pos = {first: 0}
        for i in range(1, len(tree)):
            if tree[i] == first:
                last_pos[first] = i
            else:
                second = tree[i]
                last_pos[second] = i
                break

        lo, hi = 0, i + 1
        max_fruit = cur_fruit = hi - lo
        while hi < len(tree):
            if tree[hi] == first:
                first, second = second, first
                cur_fruit += 1
            elif tree[hi] == second:
                cur_fruit += 1
            else:
                lo = last_pos[first] + 1
                last_pos.pop(first)
                first, second = second, tree[hi]
                cur_fruit = hi - lo + 1
            last_pos[second] = hi
            hi += 1
            max_fruit = max(max_fruit, cur_fruit)

        return max_fruit


# precise two pointers, slightly slower
class Solution(object):
    def totalFruit(self, tree):
        import collections

        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

# @lc code=end
