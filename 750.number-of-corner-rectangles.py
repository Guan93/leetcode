# brute force count pairs: O(m^2 * n) and O(1), TLE
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for row1 in range(m):
            for row2 in range(row1 + 1, m):
                num_pairs = 0
                for col in range(n):
                    if grid[row1][col] == 1 and grid[row2][col] == 1:
                        num_pairs += 1
                if num_pairs >= 2:
                    res += num_pairs * (num_pairs - 1) // 2
        return res


# same time complexity but get accepted: O(m * n^2) and O(n^2)
class Solution:
    def countCornerRectangles(self, grid):
        import collections

        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                # this if condition will boost the performance
                if v1:
                    for c2 in range(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans