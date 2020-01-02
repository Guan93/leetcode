# O(5 ^ num_digits) and O(5 ^ digits)
class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = [0, 1, 6, 8, 9]
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        def dfs(num, rotation, digit):
            res = 0
            if num != rotation:
                res += 1
            for d in valid:
                if d == 0 and num == 0:
                    continue
                if num * 10 + d <= N:
                    res += dfs(num * 10 + d, mapping[d] * digit + rotation, digit * 10)
            return res

        return dfs(0, 0, 1)
