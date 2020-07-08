# O(nlogn): in each recursive call, O(n) is taken for string construction;
# there are totally logn recursive calls
class Solution:
    def findContestMatch(self, n: int) -> str:
        def helper(l):
            if len(l) == 1:
                return l[0]
            new_list = []
            for i in range(len(l) // 2):
                new_list.append(f'({l[i]},{l[-(i + 1)]})')
            return helper(new_list)

        return helper([str(i + 1) for i in range(n)])